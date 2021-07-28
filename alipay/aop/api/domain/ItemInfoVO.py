#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduTrainExtInfo import EduTrainExtInfo
from alipay.aop.api.domain.CateInfoVO import CateInfoVO
from alipay.aop.api.domain.PItemInfoVO import PItemInfoVO
from alipay.aop.api.domain.CateInfoVO import CateInfoVO


class ItemInfoVO(object):

    def __init__(self):
        self._desc = None
        self._distance = None
        self._ext_info = None
        self._first_cates = None
        self._id = None
        self._is_hot = None
        self._logo = None
        self._name = None
        self._ori_price = None
        self._p_item_info = None
        self._position = None
        self._price = None
        self._scm = None
        self._secend_cates = None
        self._source_type = None
        self._tags = None
        self._time = None
        self._tips = None
        self._url = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, EduTrainExtInfo):
            self._ext_info = value
        else:
            self._ext_info = EduTrainExtInfo.from_alipay_dict(value)
    @property
    def first_cates(self):
        return self._first_cates

    @first_cates.setter
    def first_cates(self, value):
        if isinstance(value, list):
            self._first_cates = list()
            for i in value:
                if isinstance(i, CateInfoVO):
                    self._first_cates.append(i)
                else:
                    self._first_cates.append(CateInfoVO.from_alipay_dict(i))
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_hot(self):
        return self._is_hot

    @is_hot.setter
    def is_hot(self, value):
        self._is_hot = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def ori_price(self):
        return self._ori_price

    @ori_price.setter
    def ori_price(self, value):
        self._ori_price = value
    @property
    def p_item_info(self):
        return self._p_item_info

    @p_item_info.setter
    def p_item_info(self, value):
        if isinstance(value, PItemInfoVO):
            self._p_item_info = value
        else:
            self._p_item_info = PItemInfoVO.from_alipay_dict(value)
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def scm(self):
        return self._scm

    @scm.setter
    def scm(self, value):
        self._scm = value
    @property
    def secend_cates(self):
        return self._secend_cates

    @secend_cates.setter
    def secend_cates(self, value):
        if isinstance(value, list):
            self._secend_cates = list()
            for i in value:
                if isinstance(i, CateInfoVO):
                    self._secend_cates.append(i)
                else:
                    self._secend_cates.append(CateInfoVO.from_alipay_dict(i))
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
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
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        if isinstance(value, list):
            self._tips = list()
            for i in value:
                self._tips.append(i)
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.first_cates:
            if isinstance(self.first_cates, list):
                for i in range(0, len(self.first_cates)):
                    element = self.first_cates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.first_cates[i] = element.to_alipay_dict()
            if hasattr(self.first_cates, 'to_alipay_dict'):
                params['first_cates'] = self.first_cates.to_alipay_dict()
            else:
                params['first_cates'] = self.first_cates
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_hot:
            if hasattr(self.is_hot, 'to_alipay_dict'):
                params['is_hot'] = self.is_hot.to_alipay_dict()
            else:
                params['is_hot'] = self.is_hot
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.ori_price:
            if hasattr(self.ori_price, 'to_alipay_dict'):
                params['ori_price'] = self.ori_price.to_alipay_dict()
            else:
                params['ori_price'] = self.ori_price
        if self.p_item_info:
            if hasattr(self.p_item_info, 'to_alipay_dict'):
                params['p_item_info'] = self.p_item_info.to_alipay_dict()
            else:
                params['p_item_info'] = self.p_item_info
        if self.position:
            if hasattr(self.position, 'to_alipay_dict'):
                params['position'] = self.position.to_alipay_dict()
            else:
                params['position'] = self.position
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.scm:
            if hasattr(self.scm, 'to_alipay_dict'):
                params['scm'] = self.scm.to_alipay_dict()
            else:
                params['scm'] = self.scm
        if self.secend_cates:
            if isinstance(self.secend_cates, list):
                for i in range(0, len(self.secend_cates)):
                    element = self.secend_cates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.secend_cates[i] = element.to_alipay_dict()
            if hasattr(self.secend_cates, 'to_alipay_dict'):
                params['secend_cates'] = self.secend_cates.to_alipay_dict()
            else:
                params['secend_cates'] = self.secend_cates
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
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
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.tips:
            if isinstance(self.tips, list):
                for i in range(0, len(self.tips)):
                    element = self.tips[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tips[i] = element.to_alipay_dict()
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemInfoVO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'distance' in d:
            o.distance = d['distance']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'first_cates' in d:
            o.first_cates = d['first_cates']
        if 'id' in d:
            o.id = d['id']
        if 'is_hot' in d:
            o.is_hot = d['is_hot']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'ori_price' in d:
            o.ori_price = d['ori_price']
        if 'p_item_info' in d:
            o.p_item_info = d['p_item_info']
        if 'position' in d:
            o.position = d['position']
        if 'price' in d:
            o.price = d['price']
        if 'scm' in d:
            o.scm = d['scm']
        if 'secend_cates' in d:
            o.secend_cates = d['secend_cates']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'tags' in d:
            o.tags = d['tags']
        if 'time' in d:
            o.time = d['time']
        if 'tips' in d:
            o.tips = d['tips']
        if 'url' in d:
            o.url = d['url']
        return o


