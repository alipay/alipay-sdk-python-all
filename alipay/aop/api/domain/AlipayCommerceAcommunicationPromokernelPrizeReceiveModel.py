#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationPromokernelPrizeReceiveModel(object):

    def __init__(self):
        self._alipay_user_unique_identifier = None
        self._camp_id = None
        self._receive_order_ids = None

    @property
    def alipay_user_unique_identifier(self):
        return self._alipay_user_unique_identifier

    @alipay_user_unique_identifier.setter
    def alipay_user_unique_identifier(self, value):
        self._alipay_user_unique_identifier = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def receive_order_ids(self):
        return self._receive_order_ids

    @receive_order_ids.setter
    def receive_order_ids(self, value):
        if isinstance(value, list):
            self._receive_order_ids = list()
            for i in value:
                self._receive_order_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_unique_identifier:
            if hasattr(self.alipay_user_unique_identifier, 'to_alipay_dict'):
                params['alipay_user_unique_identifier'] = self.alipay_user_unique_identifier.to_alipay_dict()
            else:
                params['alipay_user_unique_identifier'] = self.alipay_user_unique_identifier
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.receive_order_ids:
            if isinstance(self.receive_order_ids, list):
                for i in range(0, len(self.receive_order_ids)):
                    element = self.receive_order_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.receive_order_ids[i] = element.to_alipay_dict()
            if hasattr(self.receive_order_ids, 'to_alipay_dict'):
                params['receive_order_ids'] = self.receive_order_ids.to_alipay_dict()
            else:
                params['receive_order_ids'] = self.receive_order_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationPromokernelPrizeReceiveModel()
        if 'alipay_user_unique_identifier' in d:
            o.alipay_user_unique_identifier = d['alipay_user_unique_identifier']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'receive_order_ids' in d:
            o.receive_order_ids = d['receive_order_ids']
        return o


