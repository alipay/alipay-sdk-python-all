#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodPrepaymentApplyModel(object):

    def __init__(self):
        self._app_seq_no = None
        self._biz_type = None
        self._cust_name = None
        self._drawdown_no = None
        self._id_card_no = None
        self._operate_mode = None
        self._prepayment_amt = None
        self._prepayment_apply_no = None
        self._prepayment_int_amt = None
        self._prepayment_pen_amt = None
        self._prepayment_prin_amt = None
        self._repay_mode = None
        self._request_id = None

    @property
    def app_seq_no(self):
        return self._app_seq_no

    @app_seq_no.setter
    def app_seq_no(self, value):
        self._app_seq_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cust_name(self):
        return self._cust_name

    @cust_name.setter
    def cust_name(self, value):
        self._cust_name = value
    @property
    def drawdown_no(self):
        return self._drawdown_no

    @drawdown_no.setter
    def drawdown_no(self, value):
        self._drawdown_no = value
    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def operate_mode(self):
        return self._operate_mode

    @operate_mode.setter
    def operate_mode(self, value):
        self._operate_mode = value
    @property
    def prepayment_amt(self):
        return self._prepayment_amt

    @prepayment_amt.setter
    def prepayment_amt(self, value):
        self._prepayment_amt = value
    @property
    def prepayment_apply_no(self):
        return self._prepayment_apply_no

    @prepayment_apply_no.setter
    def prepayment_apply_no(self, value):
        self._prepayment_apply_no = value
    @property
    def prepayment_int_amt(self):
        return self._prepayment_int_amt

    @prepayment_int_amt.setter
    def prepayment_int_amt(self, value):
        self._prepayment_int_amt = value
    @property
    def prepayment_pen_amt(self):
        return self._prepayment_pen_amt

    @prepayment_pen_amt.setter
    def prepayment_pen_amt(self, value):
        self._prepayment_pen_amt = value
    @property
    def prepayment_prin_amt(self):
        return self._prepayment_prin_amt

    @prepayment_prin_amt.setter
    def prepayment_prin_amt(self, value):
        self._prepayment_prin_amt = value
    @property
    def repay_mode(self):
        return self._repay_mode

    @repay_mode.setter
    def repay_mode(self, value):
        self._repay_mode = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_seq_no:
            if hasattr(self.app_seq_no, 'to_alipay_dict'):
                params['app_seq_no'] = self.app_seq_no.to_alipay_dict()
            else:
                params['app_seq_no'] = self.app_seq_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cust_name:
            if hasattr(self.cust_name, 'to_alipay_dict'):
                params['cust_name'] = self.cust_name.to_alipay_dict()
            else:
                params['cust_name'] = self.cust_name
        if self.drawdown_no:
            if hasattr(self.drawdown_no, 'to_alipay_dict'):
                params['drawdown_no'] = self.drawdown_no.to_alipay_dict()
            else:
                params['drawdown_no'] = self.drawdown_no
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
        if self.operate_mode:
            if hasattr(self.operate_mode, 'to_alipay_dict'):
                params['operate_mode'] = self.operate_mode.to_alipay_dict()
            else:
                params['operate_mode'] = self.operate_mode
        if self.prepayment_amt:
            if hasattr(self.prepayment_amt, 'to_alipay_dict'):
                params['prepayment_amt'] = self.prepayment_amt.to_alipay_dict()
            else:
                params['prepayment_amt'] = self.prepayment_amt
        if self.prepayment_apply_no:
            if hasattr(self.prepayment_apply_no, 'to_alipay_dict'):
                params['prepayment_apply_no'] = self.prepayment_apply_no.to_alipay_dict()
            else:
                params['prepayment_apply_no'] = self.prepayment_apply_no
        if self.prepayment_int_amt:
            if hasattr(self.prepayment_int_amt, 'to_alipay_dict'):
                params['prepayment_int_amt'] = self.prepayment_int_amt.to_alipay_dict()
            else:
                params['prepayment_int_amt'] = self.prepayment_int_amt
        if self.prepayment_pen_amt:
            if hasattr(self.prepayment_pen_amt, 'to_alipay_dict'):
                params['prepayment_pen_amt'] = self.prepayment_pen_amt.to_alipay_dict()
            else:
                params['prepayment_pen_amt'] = self.prepayment_pen_amt
        if self.prepayment_prin_amt:
            if hasattr(self.prepayment_prin_amt, 'to_alipay_dict'):
                params['prepayment_prin_amt'] = self.prepayment_prin_amt.to_alipay_dict()
            else:
                params['prepayment_prin_amt'] = self.prepayment_prin_amt
        if self.repay_mode:
            if hasattr(self.repay_mode, 'to_alipay_dict'):
                params['repay_mode'] = self.repay_mode.to_alipay_dict()
            else:
                params['repay_mode'] = self.repay_mode
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodPrepaymentApplyModel()
        if 'app_seq_no' in d:
            o.app_seq_no = d['app_seq_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cust_name' in d:
            o.cust_name = d['cust_name']
        if 'drawdown_no' in d:
            o.drawdown_no = d['drawdown_no']
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'operate_mode' in d:
            o.operate_mode = d['operate_mode']
        if 'prepayment_amt' in d:
            o.prepayment_amt = d['prepayment_amt']
        if 'prepayment_apply_no' in d:
            o.prepayment_apply_no = d['prepayment_apply_no']
        if 'prepayment_int_amt' in d:
            o.prepayment_int_amt = d['prepayment_int_amt']
        if 'prepayment_pen_amt' in d:
            o.prepayment_pen_amt = d['prepayment_pen_amt']
        if 'prepayment_prin_amt' in d:
            o.prepayment_prin_amt = d['prepayment_prin_amt']
        if 'repay_mode' in d:
            o.repay_mode = d['repay_mode']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


