#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcApplySyncModel(object):

    def __init__(self):
        self._card_expiry_date = None
        self._card_no = None
        self._card_type = None
        self._censor_info = None
        self._delivery_code = None
        self._delivery_name = None
        self._delivery_no = None
        self._device_expiry_date = None
        self._device_no = None
        self._device_status = None
        self._device_type = None
        self._order_id = None
        self._order_status = None
        self._order_update_time = None
        self._out_biz_no = None
        self._reactive_status = None

    @property
    def card_expiry_date(self):
        return self._card_expiry_date

    @card_expiry_date.setter
    def card_expiry_date(self, value):
        self._card_expiry_date = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def censor_info(self):
        return self._censor_info

    @censor_info.setter
    def censor_info(self, value):
        self._censor_info = value
    @property
    def delivery_code(self):
        return self._delivery_code

    @delivery_code.setter
    def delivery_code(self, value):
        self._delivery_code = value
    @property
    def delivery_name(self):
        return self._delivery_name

    @delivery_name.setter
    def delivery_name(self, value):
        self._delivery_name = value
    @property
    def delivery_no(self):
        return self._delivery_no

    @delivery_no.setter
    def delivery_no(self, value):
        self._delivery_no = value
    @property
    def device_expiry_date(self):
        return self._device_expiry_date

    @device_expiry_date.setter
    def device_expiry_date(self, value):
        self._device_expiry_date = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, value):
        self._device_status = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_update_time(self):
        return self._order_update_time

    @order_update_time.setter
    def order_update_time(self, value):
        self._order_update_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def reactive_status(self):
        return self._reactive_status

    @reactive_status.setter
    def reactive_status(self, value):
        self._reactive_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_expiry_date:
            if hasattr(self.card_expiry_date, 'to_alipay_dict'):
                params['card_expiry_date'] = self.card_expiry_date.to_alipay_dict()
            else:
                params['card_expiry_date'] = self.card_expiry_date
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.censor_info:
            if hasattr(self.censor_info, 'to_alipay_dict'):
                params['censor_info'] = self.censor_info.to_alipay_dict()
            else:
                params['censor_info'] = self.censor_info
        if self.delivery_code:
            if hasattr(self.delivery_code, 'to_alipay_dict'):
                params['delivery_code'] = self.delivery_code.to_alipay_dict()
            else:
                params['delivery_code'] = self.delivery_code
        if self.delivery_name:
            if hasattr(self.delivery_name, 'to_alipay_dict'):
                params['delivery_name'] = self.delivery_name.to_alipay_dict()
            else:
                params['delivery_name'] = self.delivery_name
        if self.delivery_no:
            if hasattr(self.delivery_no, 'to_alipay_dict'):
                params['delivery_no'] = self.delivery_no.to_alipay_dict()
            else:
                params['delivery_no'] = self.delivery_no
        if self.device_expiry_date:
            if hasattr(self.device_expiry_date, 'to_alipay_dict'):
                params['device_expiry_date'] = self.device_expiry_date.to_alipay_dict()
            else:
                params['device_expiry_date'] = self.device_expiry_date
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.device_status:
            if hasattr(self.device_status, 'to_alipay_dict'):
                params['device_status'] = self.device_status.to_alipay_dict()
            else:
                params['device_status'] = self.device_status
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_update_time:
            if hasattr(self.order_update_time, 'to_alipay_dict'):
                params['order_update_time'] = self.order_update_time.to_alipay_dict()
            else:
                params['order_update_time'] = self.order_update_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.reactive_status:
            if hasattr(self.reactive_status, 'to_alipay_dict'):
                params['reactive_status'] = self.reactive_status.to_alipay_dict()
            else:
                params['reactive_status'] = self.reactive_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcApplySyncModel()
        if 'card_expiry_date' in d:
            o.card_expiry_date = d['card_expiry_date']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'censor_info' in d:
            o.censor_info = d['censor_info']
        if 'delivery_code' in d:
            o.delivery_code = d['delivery_code']
        if 'delivery_name' in d:
            o.delivery_name = d['delivery_name']
        if 'delivery_no' in d:
            o.delivery_no = d['delivery_no']
        if 'device_expiry_date' in d:
            o.device_expiry_date = d['device_expiry_date']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'device_status' in d:
            o.device_status = d['device_status']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_update_time' in d:
            o.order_update_time = d['order_update_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'reactive_status' in d:
            o.reactive_status = d['reactive_status']
        return o


