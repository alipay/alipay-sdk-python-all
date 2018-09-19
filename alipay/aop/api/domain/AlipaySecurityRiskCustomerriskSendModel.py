#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskCustomerriskSendModel(object):

    def __init__(self):
        self._bank_card_no = None
        self._business_license_no = None
        self._cert_no = None
        self._email_address = None
        self._external_id = None
        self._merch_name = None
        self._mobile = None
        self._mobile_ip = None
        self._order_ip = None
        self._pid = None
        self._plat_account = None
        self._process_code = None
        self._smid = None
        self._trade_no = None

    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def merch_name(self):
        return self._merch_name

    @merch_name.setter
    def merch_name(self, value):
        self._merch_name = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def mobile_ip(self):
        return self._mobile_ip

    @mobile_ip.setter
    def mobile_ip(self, value):
        self._mobile_ip = value
    @property
    def order_ip(self):
        return self._order_ip

    @order_ip.setter
    def order_ip(self, value):
        self._order_ip = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def plat_account(self):
        return self._plat_account

    @plat_account.setter
    def plat_account(self, value):
        self._plat_account = value
    @property
    def process_code(self):
        return self._process_code

    @process_code.setter
    def process_code(self, value):
        self._process_code = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = self.business_license_no.to_alipay_dict()
            else:
                params['business_license_no'] = self.business_license_no
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.email_address:
            if hasattr(self.email_address, 'to_alipay_dict'):
                params['email_address'] = self.email_address.to_alipay_dict()
            else:
                params['email_address'] = self.email_address
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.merch_name:
            if hasattr(self.merch_name, 'to_alipay_dict'):
                params['merch_name'] = self.merch_name.to_alipay_dict()
            else:
                params['merch_name'] = self.merch_name
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.mobile_ip:
            if hasattr(self.mobile_ip, 'to_alipay_dict'):
                params['mobile_ip'] = self.mobile_ip.to_alipay_dict()
            else:
                params['mobile_ip'] = self.mobile_ip
        if self.order_ip:
            if hasattr(self.order_ip, 'to_alipay_dict'):
                params['order_ip'] = self.order_ip.to_alipay_dict()
            else:
                params['order_ip'] = self.order_ip
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.plat_account:
            if hasattr(self.plat_account, 'to_alipay_dict'):
                params['plat_account'] = self.plat_account.to_alipay_dict()
            else:
                params['plat_account'] = self.plat_account
        if self.process_code:
            if hasattr(self.process_code, 'to_alipay_dict'):
                params['process_code'] = self.process_code.to_alipay_dict()
            else:
                params['process_code'] = self.process_code
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskCustomerriskSendModel()
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'business_license_no' in d:
            o.business_license_no = d['business_license_no']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'email_address' in d:
            o.email_address = d['email_address']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'merch_name' in d:
            o.merch_name = d['merch_name']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'mobile_ip' in d:
            o.mobile_ip = d['mobile_ip']
        if 'order_ip' in d:
            o.order_ip = d['order_ip']
        if 'pid' in d:
            o.pid = d['pid']
        if 'plat_account' in d:
            o.plat_account = d['plat_account']
        if 'process_code' in d:
            o.process_code = d['process_code']
        if 'smid' in d:
            o.smid = d['smid']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


