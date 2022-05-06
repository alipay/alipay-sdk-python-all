#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ImageInfos import ImageInfos


class AlipayMsaasMediarecogMmtcapiAntigenIdentifyModel(object):

    def __init__(self):
        self._biz_id = None
        self._image_info_list = None
        self._params = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def image_info_list(self):
        return self._image_info_list

    @image_info_list.setter
    def image_info_list(self, value):
        if isinstance(value, list):
            self._image_info_list = list()
            for i in value:
                if isinstance(i, ImageInfos):
                    self._image_info_list.append(i)
                else:
                    self._image_info_list.append(ImageInfos.from_alipay_dict(i))
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.image_info_list:
            if isinstance(self.image_info_list, list):
                for i in range(0, len(self.image_info_list)):
                    element = self.image_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_info_list[i] = element.to_alipay_dict()
            if hasattr(self.image_info_list, 'to_alipay_dict'):
                params['image_info_list'] = self.image_info_list.to_alipay_dict()
            else:
                params['image_info_list'] = self.image_info_list
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcapiAntigenIdentifyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'image_info_list' in d:
            o.image_info_list = d['image_info_list']
        if 'params' in d:
            o.params = d['params']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


