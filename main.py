from pixivpy3 import *
import os
import datetime
import time
def main(Date):
    api=AppPixivAPI()
    api.login("975808264@qq.com","kqw84137553")
    json_result=api.illust_ranking('day',date=Date,req_auth=True)
    directory="downloads"

    if not os.path.exists(directory):
        os.makedirs(directory)

    for idx, illust in enumerate(json_result.illusts[:4]):
        image_url=illust.meta_single_page.get('original_image_url', illust.image_urls.large)
        print("%s %s" % (illust.title, image_url))

        if idx == 0:
            api.download(image_url, path=directory, name=None)
        elif idx == 1:
            url_basename=os.path.basename(image_url)
            extension=os.path.splitext(url_basename)[1]
            name ="illust_%d%s%s"%(illust.id, illust.title, extension)
            api.download(image_url, path=directory, name=name)
        elif idx == 2:
            api.download(image_url, path=directory, name='illust_%s.jpg' % (illust.id))

if __name__ == '__main__':
        while (1):
            now = datetime.datetime.now()
            delta = datetime.timedelta(days=-1)
            n_days = now + delta
            main(n_days.strftime("%Y-%m-%d"))
            time.sleep(86400)



