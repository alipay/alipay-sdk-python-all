#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySalaryRefundQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._out_refund_no = None
        self._participant_id = None
        self._participant_type = None
        self._product_code = None
        self._refund_order_no = None
        self._relate_order_no = None
        self._sign_xml = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
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
    def refund_order_no(self):
        return self._refund_order_no

    @refund_order_no.setter
    def refund_order_no(self, value):
        self._refund_order_no = value
    @property
    def relate_order_no(self):
        return self._relate_order_no

    @relate_order_no.setter
    def relate_order_no(self, value):
        self._relate_order_no = value
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
        if self.refund_order_no:
            if hasattr(self.refund_order_no, 'to_alipay_dict'):
                params['refund_order_no'] = self.refund_order_no.to_alipay_dict()
            else:
                params['refund_order_no'] = self.refund_order_no
        if self.relate_order_no:
            if hasattr(self.relate_order_no, 'to_alipay_dict'):
                params['relate_order_no'] = self.relate_order_no.to_alipay_dict()
            else:
                params['relate_order_no'] = self.relate_order_no
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
        o = AlipayEbppIndustrySalaryRefundQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'out_refund_no' in d:
            o.out_refund_no = d['out_refund_no']
        if 'participant_id' in d:
            o.participant_id = d['participant_id']
        if 'participant_type' in d:
            o.participant_type = d['participant_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'refund_order_no' in d:
            o.refund_order_no = d['refund_order_no']
        if 'relate_order_no' in d:
            o.relate_order_no = d['relate_order_no']
        if 'sign_xml' in d:
            o.sign_xml = d['sign_xml']
        return o


