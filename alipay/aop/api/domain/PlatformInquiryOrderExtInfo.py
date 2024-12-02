#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PlatformInquiryOrderEvaluateInfo import PlatformInquiryOrderEvaluateInfo
from alipay.aop.api.domain.PlatformPlusRegisterInfo import PlatformPlusRegisterInfo


class PlatformInquiryOrderExtInfo(object):

    def __init__(self):
        self._alipay_channel_order_flag = None
        self._approve_comment = None
        self._chat_url = None
        self._complaint = None
        self._doctor_inquiry_link_page = None
        self._invoice_url = None
        self._medical_inquiry_order_evaluate_info = None
        self._order_pid = None
        self._plus_register_info = None
        self._refund_url = None
        self._source = None

    @property
    def alipay_channel_order_flag(self):
        return self._alipay_channel_order_flag

    @alipay_channel_order_flag.setter
    def alipay_channel_order_flag(self, value):
        self._alipay_channel_order_flag = value
    @property
    def approve_comment(self):
        return self._approve_comment

    @approve_comment.setter
    def approve_comment(self, value):
        self._approve_comment = value
    @property
    def chat_url(self):
        return self._chat_url

    @chat_url.setter
    def chat_url(self, value):
        self._chat_url = value
    @property
    def complaint(self):
        return self._complaint

    @complaint.setter
    def complaint(self, value):
        self._complaint = value
    @property
    def doctor_inquiry_link_page(self):
        return self._doctor_inquiry_link_page

    @doctor_inquiry_link_page.setter
    def doctor_inquiry_link_page(self, value):
        self._doctor_inquiry_link_page = value
    @property
    def invoice_url(self):
        return self._invoice_url

    @invoice_url.setter
    def invoice_url(self, value):
        self._invoice_url = value
    @property
    def medical_inquiry_order_evaluate_info(self):
        return self._medical_inquiry_order_evaluate_info

    @medical_inquiry_order_evaluate_info.setter
    def medical_inquiry_order_evaluate_info(self, value):
        if isinstance(value, PlatformInquiryOrderEvaluateInfo):
            self._medical_inquiry_order_evaluate_info = value
        else:
            self._medical_inquiry_order_evaluate_info = PlatformInquiryOrderEvaluateInfo.from_alipay_dict(value)
    @property
    def order_pid(self):
        return self._order_pid

    @order_pid.setter
    def order_pid(self, value):
        self._order_pid = value
    @property
    def plus_register_info(self):
        return self._plus_register_info

    @plus_register_info.setter
    def plus_register_info(self, value):
        if isinstance(value, PlatformPlusRegisterInfo):
            self._plus_register_info = value
        else:
            self._plus_register_info = PlatformPlusRegisterInfo.from_alipay_dict(value)
    @property
    def refund_url(self):
        return self._refund_url

    @refund_url.setter
    def refund_url(self, value):
        self._refund_url = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_channel_order_flag:
            if hasattr(self.alipay_channel_order_flag, 'to_alipay_dict'):
                params['alipay_channel_order_flag'] = self.alipay_channel_order_flag.to_alipay_dict()
            else:
                params['alipay_channel_order_flag'] = self.alipay_channel_order_flag
        if self.approve_comment:
            if hasattr(self.approve_comment, 'to_alipay_dict'):
                params['approve_comment'] = self.approve_comment.to_alipay_dict()
            else:
                params['approve_comment'] = self.approve_comment
        if self.chat_url:
            if hasattr(self.chat_url, 'to_alipay_dict'):
                params['chat_url'] = self.chat_url.to_alipay_dict()
            else:
                params['chat_url'] = self.chat_url
        if self.complaint:
            if hasattr(self.complaint, 'to_alipay_dict'):
                params['complaint'] = self.complaint.to_alipay_dict()
            else:
                params['complaint'] = self.complaint
        if self.doctor_inquiry_link_page:
            if hasattr(self.doctor_inquiry_link_page, 'to_alipay_dict'):
                params['doctor_inquiry_link_page'] = self.doctor_inquiry_link_page.to_alipay_dict()
            else:
                params['doctor_inquiry_link_page'] = self.doctor_inquiry_link_page
        if self.invoice_url:
            if hasattr(self.invoice_url, 'to_alipay_dict'):
                params['invoice_url'] = self.invoice_url.to_alipay_dict()
            else:
                params['invoice_url'] = self.invoice_url
        if self.medical_inquiry_order_evaluate_info:
            if hasattr(self.medical_inquiry_order_evaluate_info, 'to_alipay_dict'):
                params['medical_inquiry_order_evaluate_info'] = self.medical_inquiry_order_evaluate_info.to_alipay_dict()
            else:
                params['medical_inquiry_order_evaluate_info'] = self.medical_inquiry_order_evaluate_info
        if self.order_pid:
            if hasattr(self.order_pid, 'to_alipay_dict'):
                params['order_pid'] = self.order_pid.to_alipay_dict()
            else:
                params['order_pid'] = self.order_pid
        if self.plus_register_info:
            if hasattr(self.plus_register_info, 'to_alipay_dict'):
                params['plus_register_info'] = self.plus_register_info.to_alipay_dict()
            else:
                params['plus_register_info'] = self.plus_register_info
        if self.refund_url:
            if hasattr(self.refund_url, 'to_alipay_dict'):
                params['refund_url'] = self.refund_url.to_alipay_dict()
            else:
                params['refund_url'] = self.refund_url
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlatformInquiryOrderExtInfo()
        if 'alipay_channel_order_flag' in d:
            o.alipay_channel_order_flag = d['alipay_channel_order_flag']
        if 'approve_comment' in d:
            o.approve_comment = d['approve_comment']
        if 'chat_url' in d:
            o.chat_url = d['chat_url']
        if 'complaint' in d:
            o.complaint = d['complaint']
        if 'doctor_inquiry_link_page' in d:
            o.doctor_inquiry_link_page = d['doctor_inquiry_link_page']
        if 'invoice_url' in d:
            o.invoice_url = d['invoice_url']
        if 'medical_inquiry_order_evaluate_info' in d:
            o.medical_inquiry_order_evaluate_info = d['medical_inquiry_order_evaluate_info']
        if 'order_pid' in d:
            o.order_pid = d['order_pid']
        if 'plus_register_info' in d:
            o.plus_register_info = d['plus_register_info']
        if 'refund_url' in d:
            o.refund_url = d['refund_url']
        if 'source' in d:
            o.source = d['source']
        return o


