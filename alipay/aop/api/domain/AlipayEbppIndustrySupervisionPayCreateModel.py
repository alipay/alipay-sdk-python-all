#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySupervisionPayCreateModel(object):

    def __init__(self):
        self._alipay_uid = None
        self._amount = None
        self._biz_scene = None
        self._currency = None
        self._open_id = None
        self._out_flow_id = None
        self._out_order_no = None
        self._pay_title = None
        self._payee_participant_info = None
        self._remark = None
        self._tag = None
        self._time_expire = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_flow_id(self):
        return self._out_flow_id

    @out_flow_id.setter
    def out_flow_id(self, value):
        self._out_flow_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_title(self):
        return self._pay_title

    @pay_title.setter
    def pay_title(self, value):
        self._pay_title = value
    @property
    def payee_participant_info(self):
        return self._payee_participant_info

    @payee_participant_info.setter
    def payee_participant_info(self, value):
        self._payee_participant_info = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value
    @property
    def time_expire(self):
        return self._time_expire

    @time_expire.setter
    def time_expire(self, value):
        self._time_expire = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_flow_id:
            if hasattr(self.out_flow_id, 'to_alipay_dict'):
                params['out_flow_id'] = self.out_flow_id.to_alipay_dict()
            else:
                params['out_flow_id'] = self.out_flow_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_title:
            if hasattr(self.pay_title, 'to_alipay_dict'):
                params['pay_title'] = self.pay_title.to_alipay_dict()
            else:
                params['pay_title'] = self.pay_title
        if self.payee_participant_info:
            if hasattr(self.payee_participant_info, 'to_alipay_dict'):
                params['payee_participant_info'] = self.payee_participant_info.to_alipay_dict()
            else:
                params['payee_participant_info'] = self.payee_participant_info
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        if self.time_expire:
            if hasattr(self.time_expire, 'to_alipay_dict'):
                params['time_expire'] = self.time_expire.to_alipay_dict()
            else:
                params['time_expire'] = self.time_expire
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySupervisionPayCreateModel()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'currency' in d:
            o.currency = d['currency']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_flow_id' in d:
            o.out_flow_id = d['out_flow_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_title' in d:
            o.pay_title = d['pay_title']
        if 'payee_participant_info' in d:
            o.payee_participant_info = d['payee_participant_info']
        if 'remark' in d:
            o.remark = d['remark']
        if 'tag' in d:
            o.tag = d['tag']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        return o


