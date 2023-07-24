#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BookPopularityInfo import BookPopularityInfo
from alipay.aop.api.domain.BookPriceInfo import BookPriceInfo
from alipay.aop.api.domain.BookPromoInfo import BookPromoInfo


class AlipayUserAntbookcontentBookSyncModel(object):

    def __init__(self):
        self._author = None
        self._book_finished = None
        self._book_free = None
        self._book_id = None
        self._brief = None
        self._category_name = None
        self._copyright_type = None
        self._cover_url = None
        self._create_time = None
        self._crowd_tag_list = None
        self._name = None
        self._operate_type = None
        self._popularity_info = None
        self._price_info = None
        self._promo_info = None
        self._recommend_reason = None
        self._scene_list = None
        self._sum_chapters = None
        self._sum_words = None
        self._tag_list = None
        self._update_time = None

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
    @property
    def book_finished(self):
        return self._book_finished

    @book_finished.setter
    def book_finished(self, value):
        self._book_finished = value
    @property
    def book_free(self):
        return self._book_free

    @book_free.setter
    def book_free(self, value):
        self._book_free = value
    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, value):
        self._book_id = value
    @property
    def brief(self):
        return self._brief

    @brief.setter
    def brief(self, value):
        self._brief = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
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
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def crowd_tag_list(self):
        return self._crowd_tag_list

    @crowd_tag_list.setter
    def crowd_tag_list(self, value):
        if isinstance(value, list):
            self._crowd_tag_list = list()
            for i in value:
                self._crowd_tag_list.append(i)
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
        if isinstance(value, BookPopularityInfo):
            self._popularity_info = value
        else:
            self._popularity_info = BookPopularityInfo.from_alipay_dict(value)
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, BookPriceInfo):
            self._price_info = value
        else:
            self._price_info = BookPriceInfo.from_alipay_dict(value)
    @property
    def promo_info(self):
        return self._promo_info

    @promo_info.setter
    def promo_info(self, value):
        if isinstance(value, BookPromoInfo):
            self._promo_info = value
        else:
            self._promo_info = BookPromoInfo.from_alipay_dict(value)
    @property
    def recommend_reason(self):
        return self._recommend_reason

    @recommend_reason.setter
    def recommend_reason(self, value):
        self._recommend_reason = value
    @property
    def scene_list(self):
        return self._scene_list

    @scene_list.setter
    def scene_list(self, value):
        if isinstance(value, list):
            self._scene_list = list()
            for i in value:
                self._scene_list.append(i)
    @property
    def sum_chapters(self):
        return self._sum_chapters

    @sum_chapters.setter
    def sum_chapters(self, value):
        self._sum_chapters = value
    @property
    def sum_words(self):
        return self._sum_words

    @sum_words.setter
    def sum_words(self, value):
        self._sum_words = value
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                self._tag_list.append(i)
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.author:
            if hasattr(self.author, 'to_alipay_dict'):
                params['author'] = self.author.to_alipay_dict()
            else:
                params['author'] = self.author
        if self.book_finished:
            if hasattr(self.book_finished, 'to_alipay_dict'):
                params['book_finished'] = self.book_finished.to_alipay_dict()
            else:
                params['book_finished'] = self.book_finished
        if self.book_free:
            if hasattr(self.book_free, 'to_alipay_dict'):
                params['book_free'] = self.book_free.to_alipay_dict()
            else:
                params['book_free'] = self.book_free
        if self.book_id:
            if hasattr(self.book_id, 'to_alipay_dict'):
                params['book_id'] = self.book_id.to_alipay_dict()
            else:
                params['book_id'] = self.book_id
        if self.brief:
            if hasattr(self.brief, 'to_alipay_dict'):
                params['brief'] = self.brief.to_alipay_dict()
            else:
                params['brief'] = self.brief
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
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
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.crowd_tag_list:
            if isinstance(self.crowd_tag_list, list):
                for i in range(0, len(self.crowd_tag_list)):
                    element = self.crowd_tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.crowd_tag_list[i] = element.to_alipay_dict()
            if hasattr(self.crowd_tag_list, 'to_alipay_dict'):
                params['crowd_tag_list'] = self.crowd_tag_list.to_alipay_dict()
            else:
                params['crowd_tag_list'] = self.crowd_tag_list
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
        if self.scene_list:
            if isinstance(self.scene_list, list):
                for i in range(0, len(self.scene_list)):
                    element = self.scene_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_list[i] = element.to_alipay_dict()
            if hasattr(self.scene_list, 'to_alipay_dict'):
                params['scene_list'] = self.scene_list.to_alipay_dict()
            else:
                params['scene_list'] = self.scene_list
        if self.sum_chapters:
            if hasattr(self.sum_chapters, 'to_alipay_dict'):
                params['sum_chapters'] = self.sum_chapters.to_alipay_dict()
            else:
                params['sum_chapters'] = self.sum_chapters
        if self.sum_words:
            if hasattr(self.sum_words, 'to_alipay_dict'):
                params['sum_words'] = self.sum_words.to_alipay_dict()
            else:
                params['sum_words'] = self.sum_words
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
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
        o = AlipayUserAntbookcontentBookSyncModel()
        if 'author' in d:
            o.author = d['author']
        if 'book_finished' in d:
            o.book_finished = d['book_finished']
        if 'book_free' in d:
            o.book_free = d['book_free']
        if 'book_id' in d:
            o.book_id = d['book_id']
        if 'brief' in d:
            o.brief = d['brief']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'copyright_type' in d:
            o.copyright_type = d['copyright_type']
        if 'cover_url' in d:
            o.cover_url = d['cover_url']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'crowd_tag_list' in d:
            o.crowd_tag_list = d['crowd_tag_list']
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
        if 'scene_list' in d:
            o.scene_list = d['scene_list']
        if 'sum_chapters' in d:
            o.sum_chapters = d['sum_chapters']
        if 'sum_words' in d:
            o.sum_words = d['sum_words']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


