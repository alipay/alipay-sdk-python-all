#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotDeliveryBaseInfo import IotDeliveryBaseInfo
from alipay.aop.api.domain.IotDeliveryPlayConfig import IotDeliveryPlayConfig


class IoTDeliveryPlan(object):

    def __init__(self):
        self._delivery_base_info = None
        self._delivery_booth_code = None
        self._delivery_error_msg = None
        self._delivery_id = None
        self._delivery_play_config = None
        self._delivery_status = None
        self._out_biz_no = None

    @property
    def delivery_base_info(self):
        return self._delivery_base_info

    @delivery_base_info.setter
    def delivery_base_info(self, value):
        if isinstance(value, IotDeliveryBaseInfo):
            self._delivery_base_info = value
        else:
            self._delivery_base_info = IotDeliveryBaseInfo.from_alipay_dict(value)
    @property
    def delivery_booth_code(self):
        return self._delivery_booth_code

    @delivery_booth_code.setter
    def delivery_booth_code(self, value):
        self._delivery_booth_code = value
    @property
    def delivery_error_msg(self):
        return self._delivery_error_msg

    @delivery_error_msg.setter
    def delivery_error_msg(self, value):
        self._delivery_error_msg = value
    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def delivery_play_config(self):
        return self._delivery_play_config

    @delivery_play_config.setter
    def delivery_play_config(self, value):
        if isinstance(value, IotDeliveryPlayConfig):
            self._delivery_play_config = value
        else:
            self._delivery_play_config = IotDeliveryPlayConfig.from_alipay_dict(value)
    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_base_info:
            if hasattr(self.delivery_base_info, 'to_alipay_dict'):
                params['delivery_base_info'] = self.delivery_base_info.to_alipay_dict()
            else:
                params['delivery_base_info'] = self.delivery_base_info
        if self.delivery_booth_code:
            if hasattr(self.delivery_booth_code, 'to_alipay_dict'):
                params['delivery_booth_code'] = self.delivery_booth_code.to_alipay_dict()
            else:
                params['delivery_booth_code'] = self.delivery_booth_code
        if self.delivery_error_msg:
            if hasattr(self.delivery_error_msg, 'to_alipay_dict'):
                params['delivery_error_msg'] = self.delivery_error_msg.to_alipay_dict()
            else:
                params['delivery_error_msg'] = self.delivery_error_msg
        if self.delivery_id:
            if hasattr(self.delivery_id, 'to_alipay_dict'):
                params['delivery_id'] = self.delivery_id.to_alipay_dict()
            else:
                params['delivery_id'] = self.delivery_id
        if self.delivery_play_config:
            if hasattr(self.delivery_play_config, 'to_alipay_dict'):
                params['delivery_play_config'] = self.delivery_play_config.to_alipay_dict()
            else:
                params['delivery_play_config'] = self.delivery_play_config
        if self.delivery_status:
            if hasattr(self.delivery_status, 'to_alipay_dict'):
                params['delivery_status'] = self.delivery_status.to_alipay_dict()
            else:
                params['delivery_status'] = self.delivery_status
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IoTDeliveryPlan()
        if 'delivery_base_info' in d:
            o.delivery_base_info = d['delivery_base_info']
        if 'delivery_booth_code' in d:
            o.delivery_booth_code = d['delivery_booth_code']
        if 'delivery_error_msg' in d:
            o.delivery_error_msg = d['delivery_error_msg']
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        if 'delivery_play_config' in d:
            o.delivery_play_config = d['delivery_play_config']
        if 'delivery_status' in d:
            o.delivery_status = d['delivery_status']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


