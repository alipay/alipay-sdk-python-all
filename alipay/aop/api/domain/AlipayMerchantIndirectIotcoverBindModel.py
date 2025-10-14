#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotSpeechContentConfig import IotSpeechContentConfig


class AlipayMerchantIndirectIotcoverBindModel(object):

    def __init__(self):
        self._agreement_no = None
        self._device_id = None
        self._encode_url = None
        self._merchant_name = None
        self._screen_pay_qr_link = None
        self._smid = None
        self._speech_content = None
        self._supplier_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def encode_url(self):
        return self._encode_url

    @encode_url.setter
    def encode_url(self, value):
        self._encode_url = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def screen_pay_qr_link(self):
        return self._screen_pay_qr_link

    @screen_pay_qr_link.setter
    def screen_pay_qr_link(self, value):
        self._screen_pay_qr_link = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def speech_content(self):
        return self._speech_content

    @speech_content.setter
    def speech_content(self, value):
        if isinstance(value, IotSpeechContentConfig):
            self._speech_content = value
        else:
            self._speech_content = IotSpeechContentConfig.from_alipay_dict(value)
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.encode_url:
            if hasattr(self.encode_url, 'to_alipay_dict'):
                params['encode_url'] = self.encode_url.to_alipay_dict()
            else:
                params['encode_url'] = self.encode_url
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.screen_pay_qr_link:
            if hasattr(self.screen_pay_qr_link, 'to_alipay_dict'):
                params['screen_pay_qr_link'] = self.screen_pay_qr_link.to_alipay_dict()
            else:
                params['screen_pay_qr_link'] = self.screen_pay_qr_link
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.speech_content:
            if hasattr(self.speech_content, 'to_alipay_dict'):
                params['speech_content'] = self.speech_content.to_alipay_dict()
            else:
                params['speech_content'] = self.speech_content
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectIotcoverBindModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'encode_url' in d:
            o.encode_url = d['encode_url']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'screen_pay_qr_link' in d:
            o.screen_pay_qr_link = d['screen_pay_qr_link']
        if 'smid' in d:
            o.smid = d['smid']
        if 'speech_content' in d:
            o.speech_content = d['speech_content']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


