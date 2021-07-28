#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UnfreezeExtendParams import UnfreezeExtendParams


class ZhimaCreditPeZmgoSettleUnfreezeModel(object):

    def __init__(self):
        self._agreement_id = None
        self._alipay_user_id = None
        self._biz_time = None
        self._order_title = None
        self._out_request_no = None
        self._partner_id = None
        self._unfreeze_amount = None
        self._unfreeze_extend_params = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
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
    def unfreeze_amount(self):
        return self._unfreeze_amount

    @unfreeze_amount.setter
    def unfreeze_amount(self, value):
        self._unfreeze_amount = value
    @property
    def unfreeze_extend_params(self):
        return self._unfreeze_extend_params

    @unfreeze_extend_params.setter
    def unfreeze_extend_params(self, value):
        if isinstance(value, UnfreezeExtendParams):
            self._unfreeze_extend_params = value
        else:
            self._unfreeze_extend_params = UnfreezeExtendParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
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
        if self.unfreeze_amount:
            if hasattr(self.unfreeze_amount, 'to_alipay_dict'):
                params['unfreeze_amount'] = self.unfreeze_amount.to_alipay_dict()
            else:
                params['unfreeze_amount'] = self.unfreeze_amount
        if self.unfreeze_extend_params:
            if hasattr(self.unfreeze_extend_params, 'to_alipay_dict'):
                params['unfreeze_extend_params'] = self.unfreeze_extend_params.to_alipay_dict()
            else:
                params['unfreeze_extend_params'] = self.unfreeze_extend_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeZmgoSettleUnfreezeModel()
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'unfreeze_amount' in d:
            o.unfreeze_amount = d['unfreeze_amount']
        if 'unfreeze_extend_params' in d:
            o.unfreeze_extend_params = d['unfreeze_extend_params']
        return o


