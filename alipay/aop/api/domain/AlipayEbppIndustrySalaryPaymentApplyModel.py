#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySalaryPaymentApplyModel(object):

    def __init__(self):
        self._amount = None
        self._biz_scene = None
        self._currency = None
        self._ext_info = None
        self._merchant_id = None
        self._out_trade_no = None
        self._pay_way = None
        self._payee_account_type = None
        self._payee_branch_name = None
        self._payee_card_no = None
        self._payee_cert_no = None
        self._payee_contact_line = None
        self._payee_mobile = None
        self._payee_name = None
        self._payer_card_no = None
        self._product_code = None
        self._remark = None
        self._scene_tag = None
        self._sign_xml = None
        self._type = None

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
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_way(self):
        return self._pay_way

    @pay_way.setter
    def pay_way(self, value):
        self._pay_way = value
    @property
    def payee_account_type(self):
        return self._payee_account_type

    @payee_account_type.setter
    def payee_account_type(self, value):
        self._payee_account_type = value
    @property
    def payee_branch_name(self):
        return self._payee_branch_name

    @payee_branch_name.setter
    def payee_branch_name(self, value):
        self._payee_branch_name = value
    @property
    def payee_card_no(self):
        return self._payee_card_no

    @payee_card_no.setter
    def payee_card_no(self, value):
        self._payee_card_no = value
    @property
    def payee_cert_no(self):
        return self._payee_cert_no

    @payee_cert_no.setter
    def payee_cert_no(self, value):
        self._payee_cert_no = value
    @property
    def payee_contact_line(self):
        return self._payee_contact_line

    @payee_contact_line.setter
    def payee_contact_line(self, value):
        self._payee_contact_line = value
    @property
    def payee_mobile(self):
        return self._payee_mobile

    @payee_mobile.setter
    def payee_mobile(self, value):
        self._payee_mobile = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payer_card_no(self):
        return self._payer_card_no

    @payer_card_no.setter
    def payer_card_no(self, value):
        self._payer_card_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def scene_tag(self):
        return self._scene_tag

    @scene_tag.setter
    def scene_tag(self, value):
        self._scene_tag = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_way:
            if hasattr(self.pay_way, 'to_alipay_dict'):
                params['pay_way'] = self.pay_way.to_alipay_dict()
            else:
                params['pay_way'] = self.pay_way
        if self.payee_account_type:
            if hasattr(self.payee_account_type, 'to_alipay_dict'):
                params['payee_account_type'] = self.payee_account_type.to_alipay_dict()
            else:
                params['payee_account_type'] = self.payee_account_type
        if self.payee_branch_name:
            if hasattr(self.payee_branch_name, 'to_alipay_dict'):
                params['payee_branch_name'] = self.payee_branch_name.to_alipay_dict()
            else:
                params['payee_branch_name'] = self.payee_branch_name
        if self.payee_card_no:
            if hasattr(self.payee_card_no, 'to_alipay_dict'):
                params['payee_card_no'] = self.payee_card_no.to_alipay_dict()
            else:
                params['payee_card_no'] = self.payee_card_no
        if self.payee_cert_no:
            if hasattr(self.payee_cert_no, 'to_alipay_dict'):
                params['payee_cert_no'] = self.payee_cert_no.to_alipay_dict()
            else:
                params['payee_cert_no'] = self.payee_cert_no
        if self.payee_contact_line:
            if hasattr(self.payee_contact_line, 'to_alipay_dict'):
                params['payee_contact_line'] = self.payee_contact_line.to_alipay_dict()
            else:
                params['payee_contact_line'] = self.payee_contact_line
        if self.payee_mobile:
            if hasattr(self.payee_mobile, 'to_alipay_dict'):
                params['payee_mobile'] = self.payee_mobile.to_alipay_dict()
            else:
                params['payee_mobile'] = self.payee_mobile
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payer_card_no:
            if hasattr(self.payer_card_no, 'to_alipay_dict'):
                params['payer_card_no'] = self.payer_card_no.to_alipay_dict()
            else:
                params['payer_card_no'] = self.payer_card_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.scene_tag:
            if hasattr(self.scene_tag, 'to_alipay_dict'):
                params['scene_tag'] = self.scene_tag.to_alipay_dict()
            else:
                params['scene_tag'] = self.scene_tag
        if self.sign_xml:
            if hasattr(self.sign_xml, 'to_alipay_dict'):
                params['sign_xml'] = self.sign_xml.to_alipay_dict()
            else:
                params['sign_xml'] = self.sign_xml
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySalaryPaymentApplyModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'currency' in d:
            o.currency = d['currency']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_way' in d:
            o.pay_way = d['pay_way']
        if 'payee_account_type' in d:
            o.payee_account_type = d['payee_account_type']
        if 'payee_branch_name' in d:
            o.payee_branch_name = d['payee_branch_name']
        if 'payee_card_no' in d:
            o.payee_card_no = d['payee_card_no']
        if 'payee_cert_no' in d:
            o.payee_cert_no = d['payee_cert_no']
        if 'payee_contact_line' in d:
            o.payee_contact_line = d['payee_contact_line']
        if 'payee_mobile' in d:
            o.payee_mobile = d['payee_mobile']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payer_card_no' in d:
            o.payer_card_no = d['payer_card_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'remark' in d:
            o.remark = d['remark']
        if 'scene_tag' in d:
            o.scene_tag = d['scene_tag']
        if 'sign_xml' in d:
            o.sign_xml = d['sign_xml']
        if 'type' in d:
            o.type = d['type']
        return o


