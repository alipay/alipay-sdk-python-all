#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlbumExtInfo import AlbumExtInfo
from alipay.aop.api.domain.AlbumPopularityInfo import AlbumPopularityInfo
from alipay.aop.api.domain.AlbumPriceInfo import AlbumPriceInfo
from alipay.aop.api.domain.AlbumPromoInfo import AlbumPromoInfo
from alipay.aop.api.domain.AlbumSoundInfo import AlbumSoundInfo


class AlipayUserAntbooksAlbumSyncModel(object):

    def __init__(self):
        self._album_duration = None
        self._album_finished = None
        self._album_free = None
        self._album_id = None
        self._announcer = None
        self._author = None
        self._brief = None
        self._category_list = None
        self._copyright_type = None
        self._cover_url = None
        self._cover_url_big = None
        self._cover_url_middle = None
        self._cover_url_small = None
        self._create_time = None
        self._ext_info_list = None
        self._name = None
        self._operate_type = None
        self._popularity_info = None
        self._price_info = None
        self._promo_info = None
        self._recommend_reason = None
        self._sound_list = None
        self._tags = None
        self._target_crowd_tags = None
        self._update_time = None

    @property
    def album_duration(self):
        return self._album_duration

    @album_duration.setter
    def album_duration(self, value):
        self._album_duration = value
    @property
    def album_finished(self):
        return self._album_finished

    @album_finished.setter
    def album_finished(self, value):
        self._album_finished = value
    @property
    def album_free(self):
        return self._album_free

    @album_free.setter
    def album_free(self, value):
        self._album_free = value
    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
    @property
    def announcer(self):
        return self._announcer

    @announcer.setter
    def announcer(self, value):
        self._announcer = value
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
    @property
    def brief(self):
        return self._brief

    @brief.setter
    def brief(self, value):
        self._brief = value
    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, list):
            self._category_list = list()
            for i in value:
                self._category_list.append(i)
    @property
    def copyright_type(self):
        return self._copyright_type

    @copyright_type.setter
    def copyright_type(self, value):
        self._copyright_type = value
    @property
    def cover_url(self):
        return self._cover_url

    @cover_url.setter
    def cover_url(self, value):
        self._cover_url = value
    @property
    def cover_url_big(self):
        return self._cover_url_big

    @cover_url_big.setter
    def cover_url_big(self, value):
        self._cover_url_big = value
    @property
    def cover_url_middle(self):
        return self._cover_url_middle

    @cover_url_middle.setter
    def cover_url_middle(self, value):
        self._cover_url_middle = value
    @property
    def cover_url_small(self):
        return self._cover_url_small

    @cover_url_small.setter
    def cover_url_small(self, value):
        self._cover_url_small = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def ext_info_list(self):
        return self._ext_info_list

    @ext_info_list.setter
    def ext_info_list(self, value):
        if isinstance(value, list):
            self._ext_info_list = list()
            for i in value:
                if isinstance(i, AlbumExtInfo):
                    self._ext_info_list.append(i)
                else:
                    self._ext_info_list.append(AlbumExtInfo.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def popularity_info(self):
        return self._popularity_info

    @popularity_info.setter
    def popularity_info(self, value):
        if isinstance(value, AlbumPopularityInfo):
            self._popularity_info = value
        else:
            self._popularity_info = AlbumPopularityInfo.from_alipay_dict(value)
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, AlbumPriceInfo):
            self._price_info = value
        else:
            self._price_info = AlbumPriceInfo.from_alipay_dict(value)
    @property
    def promo_info(self):
        return self._promo_info

    @promo_info.setter
    def promo_info(self, value):
        if isinstance(value, AlbumPromoInfo):
            self._promo_info = value
        else:
            self._promo_info = AlbumPromoInfo.from_alipay_dict(value)
    @property
    def recommend_reason(self):
        return self._recommend_reason

    @recommend_reason.setter
    def recommend_reason(self, value):
        self._recommend_reason = value
    @property
    def sound_list(self):
        return self._sound_list

    @sound_list.setter
    def sound_list(self, value):
        if isinstance(value, list):
            self._sound_list = list()
            for i in value:
                if isinstance(i, AlbumSoundInfo):
                    self._sound_list.append(i)
                else:
                    self._sound_list.append(AlbumSoundInfo.from_alipay_dict(i))
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)
    @property
    def target_crowd_tags(self):
        return self._target_crowd_tags

    @target_crowd_tags.setter
    def target_crowd_tags(self, value):
        if isinstance(value, list):
            self._target_crowd_tags = list()
            for i in value:
                self._target_crowd_tags.append(i)
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.album_duration:
            if hasattr(self.album_duration, 'to_alipay_dict'):
                params['album_duration'] = self.album_duration.to_alipay_dict()
            else:
                params['album_duration'] = self.album_duration
        if self.album_finished:
            if hasattr(self.album_finished, 'to_alipay_dict'):
                params['album_finished'] = self.album_finished.to_alipay_dict()
            else:
                params['album_finished'] = self.album_finished
        if self.album_free:
            if hasattr(self.album_free, 'to_alipay_dict'):
                params['album_free'] = self.album_free.to_alipay_dict()
            else:
                params['album_free'] = self.album_free
        if self.album_id:
            if hasattr(self.album_id, 'to_alipay_dict'):
                params['album_id'] = self.album_id.to_alipay_dict()
            else:
                params['album_id'] = self.album_id
        if self.announcer:
            if hasattr(self.announcer, 'to_alipay_dict'):
                params['announcer'] = self.announcer.to_alipay_dict()
            else:
                params['announcer'] = self.announcer
        if self.author:
            if hasattr(self.author, 'to_alipay_dict'):
                params['author'] = self.author.to_alipay_dict()
            else:
                params['author'] = self.author
        if self.brief:
            if hasattr(self.brief, 'to_alipay_dict'):
                params['brief'] = self.brief.to_alipay_dict()
            else:
                params['brief'] = self.brief
        if self.category_list:
            if isinstance(self.category_list, list):
                for i in range(0, len(self.category_list)):
                    element = self.category_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_list[i] = element.to_alipay_dict()
            if hasattr(self.category_list, 'to_alipay_dict'):
                params['category_list'] = self.category_list.to_alipay_dict()
            else:
                params['category_list'] = self.category_list
        if self.copyright_type:
            if hasattr(self.copyright_type, 'to_alipay_dict'):
                params['copyright_type'] = self.copyright_type.to_alipay_dict()
            else:
                params['copyright_type'] = self.copyright_type
        if self.cover_url:
            if hasattr(self.cover_url, 'to_alipay_dict'):
                params['cover_url'] = self.cover_url.to_alipay_dict()
            else:
                params['cover_url'] = self.cover_url
        if self.cover_url_big:
            if hasattr(self.cover_url_big, 'to_alipay_dict'):
                params['cover_url_big'] = self.cover_url_big.to_alipay_dict()
            else:
                params['cover_url_big'] = self.cover_url_big
        if self.cover_url_middle:
            if hasattr(self.cover_url_middle, 'to_alipay_dict'):
                params['cover_url_middle'] = self.cover_url_middle.to_alipay_dict()
            else:
                params['cover_url_middle'] = self.cover_url_middle
        if self.cover_url_small:
            if hasattr(self.cover_url_small, 'to_alipay_dict'):
                params['cover_url_small'] = self.cover_url_small.to_alipay_dict()
            else:
                params['cover_url_small'] = self.cover_url_small
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.ext_info_list:
            if isinstance(self.ext_info_list, list):
                for i in range(0, len(self.ext_info_list)):
                    element = self.ext_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info_list[i] = element.to_alipay_dict()
            if hasattr(self.ext_info_list, 'to_alipay_dict'):
                params['ext_info_list'] = self.ext_info_list.to_alipay_dict()
            else:
                params['ext_info_list'] = self.ext_info_list
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.popularity_info:
            if hasattr(self.popularity_info, 'to_alipay_dict'):
                params['popularity_info'] = self.popularity_info.to_alipay_dict()
            else:
                params['popularity_info'] = self.popularity_info
        if self.price_info:
            if hasattr(self.price_info, 'to_alipay_dict'):
                params['price_info'] = self.price_info.to_alipay_dict()
            else:
                params['price_info'] = self.price_info
        if self.promo_info:
            if hasattr(self.promo_info, 'to_alipay_dict'):
                params['promo_info'] = self.promo_info.to_alipay_dict()
            else:
                params['promo_info'] = self.promo_info
        if self.recommend_reason:
            if hasattr(self.recommend_reason, 'to_alipay_dict'):
                params['recommend_reason'] = self.recommend_reason.to_alipay_dict()
            else:
                params['recommend_reason'] = self.recommend_reason
        if self.sound_list:
            if isinstance(self.sound_list, list):
                for i in range(0, len(self.sound_list)):
                    element = self.sound_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sound_list[i] = element.to_alipay_dict()
            if hasattr(self.sound_list, 'to_alipay_dict'):
                params['sound_list'] = self.sound_list.to_alipay_dict()
            else:
                params['sound_list'] = self.sound_list
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.target_crowd_tags:
            if isinstance(self.target_crowd_tags, list):
                for i in range(0, len(self.target_crowd_tags)):
                    element = self.target_crowd_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_crowd_tags[i] = element.to_alipay_dict()
            if hasattr(self.target_crowd_tags, 'to_alipay_dict'):
                params['target_crowd_tags'] = self.target_crowd_tags.to_alipay_dict()
            else:
                params['target_crowd_tags'] = self.target_crowd_tags
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntbooksAlbumSyncModel()
        if 'album_duration' in d:
            o.album_duration = d['album_duration']
        if 'album_finished' in d:
            o.album_finished = d['album_finished']
        if 'album_free' in d:
            o.album_free = d['album_free']
        if 'album_id' in d:
            o.album_id = d['album_id']
        if 'announcer' in d:
            o.announcer = d['announcer']
        if 'author' in d:
            o.author = d['author']
        if 'brief' in d:
            o.brief = d['brief']
        if 'category_list' in d:
            o.category_list = d['category_list']
        if 'copyright_type' in d:
            o.copyright_type = d['copyright_type']
        if 'cover_url' in d:
            o.cover_url = d['cover_url']
        if 'cover_url_big' in d:
            o.cover_url_big = d['cover_url_big']
        if 'cover_url_middle' in d:
            o.cover_url_middle = d['cover_url_middle']
        if 'cover_url_small' in d:
            o.cover_url_small = d['cover_url_small']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'ext_info_list' in d:
            o.ext_info_list = d['ext_info_list']
        if 'name' in d:
            o.name = d['name']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'popularity_info' in d:
            o.popularity_info = d['popularity_info']
        if 'price_info' in d:
            o.price_info = d['price_info']
        if 'promo_info' in d:
            o.promo_info = d['promo_info']
        if 'recommend_reason' in d:
            o.recommend_reason = d['recommend_reason']
        if 'sound_list' in d:
            o.sound_list = d['sound_list']
        if 'tags' in d:
            o.tags = d['tags']
        if 'target_crowd_tags' in d:
            o.target_crowd_tags = d['target_crowd_tags']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


