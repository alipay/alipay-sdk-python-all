#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryActivityContentInfo import DeliveryActivityContentInfo
from alipay.aop.api.domain.DeliveryMiniAppContentInfo import DeliveryMiniAppContentInfo
from alipay.aop.api.domain.DeliveryDisplayInfo import DeliveryDisplayInfo
from alipay.aop.api.domain.DeliveryItemContentInfo import DeliveryItemContentInfo


class DeliveryContentInfo(object):

    def __init__(self):
        self._delivery_activity_content = None
        self._delivery_app_content = None
        self._delivery_content_type = None
        self._delivery_display_info = None
        self._delivery_item_content = None

    @property
    def delivery_activity_content(self):
        return self._delivery_activity_content

    @delivery_activity_content.setter
    def delivery_activity_content(self, value):
        if isinstance(value, DeliveryActivityContentInfo):
            self._delivery_activity_content = value
        else:
            self._delivery_activity_content = DeliveryActivityContentInfo.from_alipay_dict(value)
    @property
    def delivery_app_content(self):
        return self._delivery_app_content

    @delivery_app_content.setter
    def delivery_app_content(self, value):
        if isinstance(value, DeliveryMiniAppContentInfo):
            self._delivery_app_content = value
        else:
            self._delivery_app_content = DeliveryMiniAppContentInfo.from_alipay_dict(value)
    @property
    def delivery_content_type(self):
        return self._delivery_content_type

    @delivery_content_type.setter
    def delivery_content_type(self, value):
        self._delivery_content_type = value
    @property
    def delivery_display_info(self):
        return self._delivery_display_info

    @delivery_display_info.setter
    def delivery_display_info(self, value):
        if isinstance(value, DeliveryDisplayInfo):
            self._delivery_display_info = value
        else:
            self._delivery_display_info = DeliveryDisplayInfo.from_alipay_dict(value)
    @property
    def delivery_item_content(self):
        return self._delivery_item_content

    @delivery_item_content.setter
    def delivery_item_content(self, value):
        if isinstance(value, DeliveryItemContentInfo):
            self._delivery_item_content = value
        else:
            self._delivery_item_content = DeliveryItemContentInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_activity_content:
            if hasattr(self.delivery_activity_content, 'to_alipay_dict'):
                params['delivery_activity_content'] = self.delivery_activity_content.to_alipay_dict()
            else:
                params['delivery_activity_content'] = self.delivery_activity_content
        if self.delivery_app_content:
            if hasattr(self.delivery_app_content, 'to_alipay_dict'):
                params['delivery_app_content'] = self.delivery_app_content.to_alipay_dict()
            else:
                params['delivery_app_content'] = self.delivery_app_content
        if self.delivery_content_type:
            if hasattr(self.delivery_content_type, 'to_alipay_dict'):
                params['delivery_content_type'] = self.delivery_content_type.to_alipay_dict()
            else:
                params['delivery_content_type'] = self.delivery_content_type
        if self.delivery_display_info:
            if hasattr(self.delivery_display_info, 'to_alipay_dict'):
                params['delivery_display_info'] = self.delivery_display_info.to_alipay_dict()
            else:
                params['delivery_display_info'] = self.delivery_display_info
        if self.delivery_item_content:
            if hasattr(self.delivery_item_content, 'to_alipay_dict'):
                params['delivery_item_content'] = self.delivery_item_content.to_alipay_dict()
            else:
                params['delivery_item_content'] = self.delivery_item_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryContentInfo()
        if 'delivery_activity_content' in d:
            o.delivery_activity_content = d['delivery_activity_content']
        if 'delivery_app_content' in d:
            o.delivery_app_content = d['delivery_app_content']
        if 'delivery_content_type' in d:
            o.delivery_content_type = d['delivery_content_type']
        if 'delivery_display_info' in d:
            o.delivery_display_info = d['delivery_display_info']
        if 'delivery_item_content' in d:
            o.delivery_item_content = d['delivery_item_content']
        return o


