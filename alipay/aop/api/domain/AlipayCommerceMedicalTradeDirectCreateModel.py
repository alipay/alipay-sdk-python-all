#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubMerchantInfo import SubMerchantInfo


class AlipayCommerceMedicalTradeDirectCreateModel(object):

    def __init__(self):
        self._aq_open_id = None
        self._call_back_url = None
        self._ch_info = None
        self._channel_code = None
        self._gmt_out_create = None
        self._gmt_time_expire = None
        self._open_id = None
        self._order_type = None
        self._out_trade_no = None
        self._scene_info = None
        self._service_type = None
        self._sub_merchant = None
        self._sub_service_type = None
        self._subject = None
        self._total_amount = None
        self._user_id = None

    @property
    def aq_open_id(self):
        return self._aq_open_id

    @aq_open_id.setter
    def aq_open_id(self, value):
        self._aq_open_id = value
    @property
    def call_back_url(self):
        return self._call_back_url

    @call_back_url.setter
    def call_back_url(self, value):
        self._call_back_url = value
    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def gmt_out_create(self):
        return self._gmt_out_create

    @gmt_out_create.setter
    def gmt_out_create(self, value):
        self._gmt_out_create = value
    @property
    def gmt_time_expire(self):
        return self._gmt_time_expire

    @gmt_time_expire.setter
    def gmt_time_expire(self, value):
        self._gmt_time_expire = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def scene_info(self):
        return self._scene_info

    @scene_info.setter
    def scene_info(self, value):
        self._scene_info = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, SubMerchantInfo):
            self._sub_merchant = value
        else:
            self._sub_merchant = SubMerchantInfo.from_alipay_dict(value)
    @property
    def sub_service_type(self):
        return self._sub_service_type

    @sub_service_type.setter
    def sub_service_type(self, value):
        self._sub_service_type = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aq_open_id:
            if hasattr(self.aq_open_id, 'to_alipay_dict'):
                params['aq_open_id'] = self.aq_open_id.to_alipay_dict()
            else:
                params['aq_open_id'] = self.aq_open_id
        if self.call_back_url:
            if hasattr(self.call_back_url, 'to_alipay_dict'):
                params['call_back_url'] = self.call_back_url.to_alipay_dict()
            else:
                params['call_back_url'] = self.call_back_url
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.gmt_out_create:
            if hasattr(self.gmt_out_create, 'to_alipay_dict'):
                params['gmt_out_create'] = self.gmt_out_create.to_alipay_dict()
            else:
                params['gmt_out_create'] = self.gmt_out_create
        if self.gmt_time_expire:
            if hasattr(self.gmt_time_expire, 'to_alipay_dict'):
                params['gmt_time_expire'] = self.gmt_time_expire.to_alipay_dict()
            else:
                params['gmt_time_expire'] = self.gmt_time_expire
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.scene_info:
            if hasattr(self.scene_info, 'to_alipay_dict'):
                params['scene_info'] = self.scene_info.to_alipay_dict()
            else:
                params['scene_info'] = self.scene_info
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        if self.sub_service_type:
            if hasattr(self.sub_service_type, 'to_alipay_dict'):
                params['sub_service_type'] = self.sub_service_type.to_alipay_dict()
            else:
                params['sub_service_type'] = self.sub_service_type
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
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
        o = AlipayCommerceMedicalTradeDirectCreateModel()
        if 'aq_open_id' in d:
            o.aq_open_id = d['aq_open_id']
        if 'call_back_url' in d:
            o.call_back_url = d['call_back_url']
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'gmt_out_create' in d:
            o.gmt_out_create = d['gmt_out_create']
        if 'gmt_time_expire' in d:
            o.gmt_time_expire = d['gmt_time_expire']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'scene_info' in d:
            o.scene_info = d['scene_info']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'sub_service_type' in d:
            o.sub_service_type = d['sub_service_type']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


