#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduPrizeCustomDisplayInfo import EduPrizeCustomDisplayInfo


class EduMpPrizeSendOrder(object):

    def __init__(self):
        self._camp_id = None
        self._camp_order_id = None
        self._prize_custom_display_info = None
        self._prize_id = None
        self._prize_name = None
        self._send_order_id = None
        self._send_status = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def camp_order_id(self):
        return self._camp_order_id

    @camp_order_id.setter
    def camp_order_id(self, value):
        self._camp_order_id = value
    @property
    def prize_custom_display_info(self):
        return self._prize_custom_display_info

    @prize_custom_display_info.setter
    def prize_custom_display_info(self, value):
        if isinstance(value, EduPrizeCustomDisplayInfo):
            self._prize_custom_display_info = value
        else:
            self._prize_custom_display_info = EduPrizeCustomDisplayInfo.from_alipay_dict(value)
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def send_order_id(self):
        return self._send_order_id

    @send_order_id.setter
    def send_order_id(self, value):
        self._send_order_id = value
    @property
    def send_status(self):
        return self._send_status

    @send_status.setter
    def send_status(self, value):
        self._send_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.camp_order_id:
            if hasattr(self.camp_order_id, 'to_alipay_dict'):
                params['camp_order_id'] = self.camp_order_id.to_alipay_dict()
            else:
                params['camp_order_id'] = self.camp_order_id
        if self.prize_custom_display_info:
            if hasattr(self.prize_custom_display_info, 'to_alipay_dict'):
                params['prize_custom_display_info'] = self.prize_custom_display_info.to_alipay_dict()
            else:
                params['prize_custom_display_info'] = self.prize_custom_display_info
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.send_order_id:
            if hasattr(self.send_order_id, 'to_alipay_dict'):
                params['send_order_id'] = self.send_order_id.to_alipay_dict()
            else:
                params['send_order_id'] = self.send_order_id
        if self.send_status:
            if hasattr(self.send_status, 'to_alipay_dict'):
                params['send_status'] = self.send_status.to_alipay_dict()
            else:
                params['send_status'] = self.send_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduMpPrizeSendOrder()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'camp_order_id' in d:
            o.camp_order_id = d['camp_order_id']
        if 'prize_custom_display_info' in d:
            o.prize_custom_display_info = d['prize_custom_display_info']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'send_order_id' in d:
            o.send_order_id = d['send_order_id']
        if 'send_status' in d:
            o.send_status = d['send_status']
        return o


