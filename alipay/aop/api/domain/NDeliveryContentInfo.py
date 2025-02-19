#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NDeliveryAppContent import NDeliveryAppContent
from alipay.aop.api.domain.NDeliveryDisplayInfo import NDeliveryDisplayInfo


class NDeliveryContentInfo(object):

    def __init__(self):
        self._n_delivery_app_content = None
        self._n_delivery_content_type = None
        self._n_delivery_display_info = None

    @property
    def n_delivery_app_content(self):
        return self._n_delivery_app_content

    @n_delivery_app_content.setter
    def n_delivery_app_content(self, value):
        if isinstance(value, NDeliveryAppContent):
            self._n_delivery_app_content = value
        else:
            self._n_delivery_app_content = NDeliveryAppContent.from_alipay_dict(value)
    @property
    def n_delivery_content_type(self):
        return self._n_delivery_content_type

    @n_delivery_content_type.setter
    def n_delivery_content_type(self, value):
        self._n_delivery_content_type = value
    @property
    def n_delivery_display_info(self):
        return self._n_delivery_display_info

    @n_delivery_display_info.setter
    def n_delivery_display_info(self, value):
        if isinstance(value, NDeliveryDisplayInfo):
            self._n_delivery_display_info = value
        else:
            self._n_delivery_display_info = NDeliveryDisplayInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.n_delivery_app_content:
            if hasattr(self.n_delivery_app_content, 'to_alipay_dict'):
                params['n_delivery_app_content'] = self.n_delivery_app_content.to_alipay_dict()
            else:
                params['n_delivery_app_content'] = self.n_delivery_app_content
        if self.n_delivery_content_type:
            if hasattr(self.n_delivery_content_type, 'to_alipay_dict'):
                params['n_delivery_content_type'] = self.n_delivery_content_type.to_alipay_dict()
            else:
                params['n_delivery_content_type'] = self.n_delivery_content_type
        if self.n_delivery_display_info:
            if hasattr(self.n_delivery_display_info, 'to_alipay_dict'):
                params['n_delivery_display_info'] = self.n_delivery_display_info.to_alipay_dict()
            else:
                params['n_delivery_display_info'] = self.n_delivery_display_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NDeliveryContentInfo()
        if 'n_delivery_app_content' in d:
            o.n_delivery_app_content = d['n_delivery_app_content']
        if 'n_delivery_content_type' in d:
            o.n_delivery_content_type = d['n_delivery_content_type']
        if 'n_delivery_display_info' in d:
            o.n_delivery_display_info = d['n_delivery_display_info']
        return o


