#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FulfillmentAdditionalMediaInfo import FulfillmentAdditionalMediaInfo


class AlipayCommerceRentAdditionalUploadModel(object):

    def __init__(self):
        self._fulfillment_additional_media_list = None
        self._order_id = None

    @property
    def fulfillment_additional_media_list(self):
        return self._fulfillment_additional_media_list

    @fulfillment_additional_media_list.setter
    def fulfillment_additional_media_list(self, value):
        if isinstance(value, list):
            self._fulfillment_additional_media_list = list()
            for i in value:
                if isinstance(i, FulfillmentAdditionalMediaInfo):
                    self._fulfillment_additional_media_list.append(i)
                else:
                    self._fulfillment_additional_media_list.append(FulfillmentAdditionalMediaInfo.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_additional_media_list:
            if isinstance(self.fulfillment_additional_media_list, list):
                for i in range(0, len(self.fulfillment_additional_media_list)):
                    element = self.fulfillment_additional_media_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fulfillment_additional_media_list[i] = element.to_alipay_dict()
            if hasattr(self.fulfillment_additional_media_list, 'to_alipay_dict'):
                params['fulfillment_additional_media_list'] = self.fulfillment_additional_media_list.to_alipay_dict()
            else:
                params['fulfillment_additional_media_list'] = self.fulfillment_additional_media_list
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentAdditionalUploadModel()
        if 'fulfillment_additional_media_list' in d:
            o.fulfillment_additional_media_list = d['fulfillment_additional_media_list']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o


