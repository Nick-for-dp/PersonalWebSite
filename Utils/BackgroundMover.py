from removebg import RemoveBg


if __name__ == '__main__':
    remover = RemoveBg(api_key="BmmnRtNmiSQ9Pu3QDYrqWuyJ",
                       error_log_file="E:/PersonalWebsite/logs/error.log")
    remover.remove_background_from_img_file("E:/PersonalWebsite/website/src/main/resources/templates/woo.JPG")
