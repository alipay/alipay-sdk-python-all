#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCharityForestsendpicSendModel(object):

    def __init__(self):
        self._forest_id = None
        self._out_biz_no = None
        self._pic_ext_info = None
        self._pic_url = None
        self._shoot_time = None

    @property
    def forest_id(self):
        return self._forest_id

    @forest_id.setter
    def forest_id(self, value):
        self._forest_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pic_ext_info(self):
        return self._pic_ext_info

    @pic_ext_info.setter
    def pic_ext_info(self, value):
        self._pic_ext_info = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def shoot_time(self):
        return self._shoot_time

    @shoot_time.setter
    def shoot_time(self, value):
        self._shoot_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.forest_id:
            if hasattr(self.forest_id, 'to_alipay_dict'):
                params['forest_id'] = self.forest_id.to_alipay_dict()
            else:
                params['forest_id'] = self.forest_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pic_ext_info:
            if hasattr(self.pic_ext_info, 'to_alipay_dict'):
                params['pic_ext_info'] = self.pic_ext_info.to_alipay_dict()
            else:
                params['pic_ext_info'] = self.pic_ext_info
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.shoot_time:
            if hasattr(self.shoot_time, 'to_alipay_dict'):
                params['shoot_time'] = self.shoot_time.to_alipay_dict()
            else:
                params['shoot_time'] = self.shoot_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCharityForestsendpicSendModel()
        if 'forest_id' in d:
            o.forest_id = d['forest_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pic_ext_info' in d:
            o.pic_ext_info = d['pic_ext_info']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'shoot_time' in d:
            o.shoot_time = d['shoot_time']
        return o


