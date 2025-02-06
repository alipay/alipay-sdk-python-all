#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySalaryRefundApplyModel(object):

    def __init__(self):
        self._biz_scene = None
        self._currency = None
        self._ext_info = None
        self._memo = None
        self._out_refund_no = None
        self._participant_id = None
        self._participant_type = None
        self._product_code = None
        self._refund_amount = None
        self._refund_reason = None
        self._relate_order_no = None
        self._relate_trans_no = None
        self._sign_xml = None

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
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value
    @property
    def participant_type(self):
        return self._participant_type

    @participant_type.setter
    def participant_type(self, value):
        self._participant_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def relate_order_no(self):
        return self._relate_order_no

    @relate_order_no.setter
    def relate_order_no(self, value):
        self._relate_order_no = value
    @property
    def relate_trans_no(self):
        return self._relate_trans_no

    @relate_trans_no.setter
    def relate_trans_no(self, value):
        self._relate_trans_no = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_refund_no:
            if hasattr(self.out_refund_no, 'to_alipay_dict'):
                params['out_refund_no'] = self.out_refund_no.to_alipay_dict()
            else:
                params['out_refund_no'] = self.out_refund_no
        if self.participant_id:
            if hasattr(self.participant_id, 'to_alipay_dict'):
                params['participant_id'] = self.participant_id.to_alipay_dict()
            else:
                params['participant_id'] = self.participant_id
        if self.participant_type:
            if hasattr(self.participant_type, 'to_alipay_dict'):
                params['participant_type'] = self.participant_type.to_alipay_dict()
            else:
                params['participant_type'] = self.participant_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.relate_order_no:
            if hasattr(self.relate_order_no, 'to_alipay_dict'):
                params['relate_order_no'] = self.relate_order_no.to_alipay_dict()
            else:
                params['relate_order_no'] = self.relate_order_no
        if self.relate_trans_no:
            if hasattr(self.relate_trans_no, 'to_alipay_dict'):
                params['relate_trans_no'] = self.relate_trans_no.to_alipay_dict()
            else:
                params['relate_trans_no'] = self.relate_trans_no
        if self.sign_xml:
            if hasattr(self.sign_xml, 'to_alipay_dict'):
                params['sign_xml'] = self.sign_xml.to_alipay_dict()
            else:
                params['sign_xml'] = self.sign_xml
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySalaryRefundApplyModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'currency' in d:
            o.currency = d['currency']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_refund_no' in d:
            o.out_refund_no = d['out_refund_no']
        if 'participant_id' in d:
            o.participant_id = d['participant_id']
        if 'participant_type' in d:
            o.participant_type = d['participant_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'relate_order_no' in d:
            o.relate_order_no = d['relate_order_no']
        if 'relate_trans_no' in d:
            o.relate_trans_no = d['relate_trans_no']
        if 'sign_xml' in d:
            o.sign_xml = d['sign_xml']
        return o


