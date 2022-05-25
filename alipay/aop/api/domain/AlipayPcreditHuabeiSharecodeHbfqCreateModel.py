#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FQExtendParams import FQExtendParams


class AlipayPcreditHuabeiSharecodeHbfqCreateModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._biz_link = None
        self._biz_scene = None
        self._ext_info = None
        self._out_request_no = None
        self._partner_id = None
        self._pay_amount = None
        self._seller_id = None
        self._source = None
        self._sub_merchant_id = None
        self._time_out = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_link(self):
        return self._biz_link

    @biz_link.setter
    def biz_link(self, value):
        self._biz_link = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, FQExtendParams):
            self._ext_info = value
        else:
            self._ext_info = FQExtendParams.from_alipay_dict(value)
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value
    @property
    def time_out(self):
        return self._time_out

    @time_out.setter
    def time_out(self, value):
        self._time_out = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_link:
            if hasattr(self.biz_link, 'to_alipay_dict'):
                params['biz_link'] = self.biz_link.to_alipay_dict()
            else:
                params['biz_link'] = self.biz_link
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        if self.time_out:
            if hasattr(self.time_out, 'to_alipay_dict'):
                params['time_out'] = self.time_out.to_alipay_dict()
            else:
                params['time_out'] = self.time_out
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiSharecodeHbfqCreateModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_link' in d:
            o.biz_link = d['biz_link']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'source' in d:
            o.source = d['source']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'time_out' in d:
            o.time_out = d['time_out']
        return o


