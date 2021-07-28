#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceHellobikeSiteSubmitModel(object):

    def __init__(self):
        self._app_version = None
        self._city = None
        self._end_date = None
        self._exc_fence = None
        self._exc_poi = None
        self._ext_param = None
        self._fence = None
        self._num = None
        self._rec_poi = None
        self._size = None
        self._title = None
        self._type = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def exc_fence(self):
        return self._exc_fence

    @exc_fence.setter
    def exc_fence(self, value):
        if isinstance(value, list):
            self._exc_fence = list()
            for i in value:
                self._exc_fence.append(i)
    @property
    def exc_poi(self):
        return self._exc_poi

    @exc_poi.setter
    def exc_poi(self, value):
        if isinstance(value, list):
            self._exc_poi = list()
            for i in value:
                self._exc_poi.append(i)
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def fence(self):
        return self._fence

    @fence.setter
    def fence(self, value):
        if isinstance(value, list):
            self._fence = list()
            for i in value:
                self._fence.append(i)
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def rec_poi(self):
        return self._rec_poi

    @rec_poi.setter
    def rec_poi(self, value):
        if isinstance(value, list):
            self._rec_poi = list()
            for i in value:
                self._rec_poi.append(i)
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.exc_fence:
            if isinstance(self.exc_fence, list):
                for i in range(0, len(self.exc_fence)):
                    element = self.exc_fence[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exc_fence[i] = element.to_alipay_dict()
            if hasattr(self.exc_fence, 'to_alipay_dict'):
                params['exc_fence'] = self.exc_fence.to_alipay_dict()
            else:
                params['exc_fence'] = self.exc_fence
        if self.exc_poi:
            if isinstance(self.exc_poi, list):
                for i in range(0, len(self.exc_poi)):
                    element = self.exc_poi[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exc_poi[i] = element.to_alipay_dict()
            if hasattr(self.exc_poi, 'to_alipay_dict'):
                params['exc_poi'] = self.exc_poi.to_alipay_dict()
            else:
                params['exc_poi'] = self.exc_poi
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.fence:
            if isinstance(self.fence, list):
                for i in range(0, len(self.fence)):
                    element = self.fence[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fence[i] = element.to_alipay_dict()
            if hasattr(self.fence, 'to_alipay_dict'):
                params['fence'] = self.fence.to_alipay_dict()
            else:
                params['fence'] = self.fence
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.rec_poi:
            if isinstance(self.rec_poi, list):
                for i in range(0, len(self.rec_poi)):
                    element = self.rec_poi[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rec_poi[i] = element.to_alipay_dict()
            if hasattr(self.rec_poi, 'to_alipay_dict'):
                params['rec_poi'] = self.rec_poi.to_alipay_dict()
            else:
                params['rec_poi'] = self.rec_poi
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceHellobikeSiteSubmitModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'city' in d:
            o.city = d['city']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'exc_fence' in d:
            o.exc_fence = d['exc_fence']
        if 'exc_poi' in d:
            o.exc_poi = d['exc_poi']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'fence' in d:
            o.fence = d['fence']
        if 'num' in d:
            o.num = d['num']
        if 'rec_poi' in d:
            o.rec_poi = d['rec_poi']
        if 'size' in d:
            o.size = d['size']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o


