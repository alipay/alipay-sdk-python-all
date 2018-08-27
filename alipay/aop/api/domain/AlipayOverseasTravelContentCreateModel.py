#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentPoiData import ContentPoiData


class AlipayOverseasTravelContentCreateModel(object):

    def __init__(self):
        self._author = None
        self._category_code = None
        self._category_name = None
        self._content = None
        self._content_id = None
        self._cover = None
        self._detail_url = None
        self._image_list = None
        self._modified_date = None
        self._poi_list = None
        self._publish_date = None
        self._tag_list = None
        self._title = None

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                self._image_list.append(i)
    @property
    def modified_date(self):
        return self._modified_date

    @modified_date.setter
    def modified_date(self, value):
        self._modified_date = value
    @property
    def poi_list(self):
        return self._poi_list

    @poi_list.setter
    def poi_list(self, value):
        if isinstance(value, list):
            self._poi_list = list()
            for i in value:
                if isinstance(i, ContentPoiData):
                    self._poi_list.append(i)
                else:
                    self._poi_list.append(ContentPoiData.from_alipay_dict(i))
    @property
    def publish_date(self):
        return self._publish_date

    @publish_date.setter
    def publish_date(self, value):
        self._publish_date = value
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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.author:
            if hasattr(self.author, 'to_alipay_dict'):
                params['author'] = self.author.to_alipay_dict()
            else:
                params['author'] = self.author
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.image_list:
            if isinstance(self.image_list, list):
                for i in range(0, len(self.image_list)):
                    element = self.image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_list[i] = element.to_alipay_dict()
            if hasattr(self.image_list, 'to_alipay_dict'):
                params['image_list'] = self.image_list.to_alipay_dict()
            else:
                params['image_list'] = self.image_list
        if self.modified_date:
            if hasattr(self.modified_date, 'to_alipay_dict'):
                params['modified_date'] = self.modified_date.to_alipay_dict()
            else:
                params['modified_date'] = self.modified_date
        if self.poi_list:
            if isinstance(self.poi_list, list):
                for i in range(0, len(self.poi_list)):
                    element = self.poi_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.poi_list[i] = element.to_alipay_dict()
            if hasattr(self.poi_list, 'to_alipay_dict'):
                params['poi_list'] = self.poi_list.to_alipay_dict()
            else:
                params['poi_list'] = self.poi_list
        if self.publish_date:
            if hasattr(self.publish_date, 'to_alipay_dict'):
                params['publish_date'] = self.publish_date.to_alipay_dict()
            else:
                params['publish_date'] = self.publish_date
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
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelContentCreateModel()
        if 'author' in d:
            o.author = d['author']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'content' in d:
            o.content = d['content']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'cover' in d:
            o.cover = d['cover']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'image_list' in d:
            o.image_list = d['image_list']
        if 'modified_date' in d:
            o.modified_date = d['modified_date']
        if 'poi_list' in d:
            o.poi_list = d['poi_list']
        if 'publish_date' in d:
            o.publish_date = d['publish_date']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        if 'title' in d:
            o.title = d['title']
        return o


