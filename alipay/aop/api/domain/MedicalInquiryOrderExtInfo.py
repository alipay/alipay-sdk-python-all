#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalInquiryOrderExtInfo(object):

    def __init__(self):
        self._alipay_channel_order_flag = None
        self._approve_comment = None
        self._doctor_inquiry_link_page = None
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
    def doctor_inquiry_link_page(self):
        return self._doctor_inquiry_link_page

    @doctor_inquiry_link_page.setter
    def doctor_inquiry_link_page(self, value):
        self._doctor_inquiry_link_page = value
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
        if self.doctor_inquiry_link_page:
            if hasattr(self.doctor_inquiry_link_page, 'to_alipay_dict'):
                params['doctor_inquiry_link_page'] = self.doctor_inquiry_link_page.to_alipay_dict()
            else:
                params['doctor_inquiry_link_page'] = self.doctor_inquiry_link_page
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
        o = MedicalInquiryOrderExtInfo()
        if 'alipay_channel_order_flag' in d:
            o.alipay_channel_order_flag = d['alipay_channel_order_flag']
        if 'approve_comment' in d:
            o.approve_comment = d['approve_comment']
        if 'doctor_inquiry_link_page' in d:
            o.doctor_inquiry_link_page = d['doctor_inquiry_link_page']
        if 'source' in d:
            o.source = d['source']
        return o


