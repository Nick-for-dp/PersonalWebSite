import json
import math
import requests


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    return not (73.66 < lng < 135.05 and 3.86 < lat < 53.55)


class CoordinateUtils:
    def __init__(self):
        self.token = "e49b085c9f95deebcd7253ad93b7d012"
        self.pi = 3.1415926535897932384626
        self.a = 6378245.0  # 长半轴
        self.ee = 0.00669342162296594323  # 偏心率平方
        self.earth_rad = 6378137.0

    def geocode(self, address):
        url = "https://restapi.amap.com/v3/geocode/geo?address={0}&output=JSON&key={1}".format(
            address,
            self.token
        )
        try:
            response = requests.get(url)
            geocodes = response.json()["geocodes"][0]
            lng = float(geocodes.get('location').split(',')[0])
            lat = float(geocodes.get('location').split(',')[1])
            return [lng, lat]
        except requests.exceptions.ConnectionError:
            print("高德地图API请求失败......")
            return [120.155070, 30.274084]
        except json.decoder.JSONDecodeError:
            print("高德地图API解析JSON格式失败，请检查请求url......")
            return [120.155070, 30.274084]
        finally:
            print("本次请求结束......")

    def transform_lat(self, lng, lat):
        ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
              0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
        ret += (20.0 * math.sin(6.0 * lng * self.pi) + 20.0 *
                math.sin(2.0 * lng * self.pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(lat * self.pi) + 40.0 *
                math.sin(lat / 3.0 * self.pi)) * 2.0 / 3.0
        ret += (160.0 * math.sin(lat / 12.0 * self.pi) + 320 *
                math.sin(lat * self.pi / 30.0)) * 2.0 / 3.0
        return ret

    def transform_lng(self, lng, lat):
        ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
              0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
        ret += (20.0 * math.sin(6.0 * lng * self.pi) + 20.0 *
                math.sin(2.0 * lng * self.pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(lng * self.pi) + 40.0 *
                math.sin(lng / 3.0 * self.pi)) * 2.0 / 3.0
        ret += (150.0 * math.sin(lng / 12.0 * self.pi) + 300.0 *
                math.sin(lng / 30.0 * self.pi)) * 2.0 / 3.0
        return ret

    def gcj02_to_wgs84(self, lng, lat):
        """
        GCJ02(火星坐标系)转GPS84
        :param lng:火星坐标系的经度
        :param lat:火星坐标系纬度
        :return:
        """
        if out_of_china(lng, lat):
            return [lng, lat]
        dlat = self.transform_lat(lng - 105.0, lat - 35.0)
        dlng = self.transform_lng(lng - 105.0, lat - 35.0)
        radlat = lat / 180.0 * self.pi
        magic = math.sin(radlat)
        magic = 1 - self.ee * magic * magic
        sqrtmagic = math.sqrt(magic)
        dlat = (dlat * 180.0) / ((self.a * (1 - self.ee)) / (magic * sqrtmagic) * self.pi)
        dlng = (dlng * 180.0) / (self.a / sqrtmagic * math.cos(radlat) * self.pi)
        mglat = lat + dlat
        mglng = lng + dlng
        return [lng * 2 - mglng, lat * 2 - mglat]

    def wgs84_to_mercator(self, lng, lat):
        """
        wgs84投影坐标系转化为墨卡托地理坐标系
        :param lng: 经度
        :param lat: 纬度
        :return: 墨卡托坐标系下的(x,y)
        """
        x = lng * self.pi / 180 * self.earth_rad
        a = lat * self.pi / 180
        y = self.earth_rad / 2 * math.log((1.0 + math.sin(a)) / (1.0 - math.sin(a)))
        return [x, y]


if __name__ == '__main__':
    coordinateUtils = CoordinateUtils()
    lng, lat = coordinateUtils.geocode("湖州市德清县乾元镇")
    lng_84, lat_84 = coordinateUtils.gcj02_to_wgs84(lng, lat)
    x, y = coordinateUtils.wgs84_to_mercator(lng_84, lat_84)
    print(x, y)
