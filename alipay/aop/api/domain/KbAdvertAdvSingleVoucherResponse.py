#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertAdvContentResponse import KbAdvertAdvContentResponse
from alipay.aop.api.domain.KbAdvertAdvContent import KbAdvertAdvContent
from alipay.aop.api.domain.KbAdvertSubjectVoucherResponse import KbAdvertSubjectVoucherResponse


class KbAdvertAdvSingleVoucherResponse(object):

    def __init__(self):
        self._adv_content_list = None
        self._content = None
        self._voucher = None

    @property
    def adv_content_list(self):
        return self._adv_content_list

    @adv_content_list.setter
    def adv_content_list(self, value):
        if isinstance(value, list):
            self._adv_content_list = list()
            for i in value:
                if isinstance(i, KbAdvertAdvContentResponse):
                    self._adv_content_list.append(i)
                else:
                    self._adv_content_list.append(KbAdvertAdvContentResponse.from_alipay_dict(i))
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, KbAdvertAdvContent):
            self._content = value
        else:
            self._content = KbAdvertAdvContent.from_alipay_dict(value)
    @property
    def voucher(self):
        return self._voucher

    @voucher.setter
    def voucher(self, value):
        if isinstance(value, KbAdvertSubjectVoucherResponse):
            self._voucher = value
        else:
            self._voucher = KbAdvertSubjectVoucherResponse.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.adv_content_list:
            if isinstance(self.adv_content_list, list):
                for i in range(0, len(self.adv_content_list)):
                    element = self.adv_content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.adv_content_list[i] = element.to_alipay_dict()
            if hasattr(self.adv_content_list, 'to_alipay_dict'):
                params['adv_content_list'] = self.adv_content_list.to_alipay_dict()
            else:
                params['adv_content_list'] = self.adv_content_list
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.voucher:
            if hasattr(self.voucher, 'to_alipay_dict'):
                params['voucher'] = self.voucher.to_alipay_dict()
            else:
                params['voucher'] = self.voucher
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertAdvSingleVoucherResponse()
        if 'adv_content_list' in d:
            o.adv_content_list = d['adv_content_list']
        if 'content' in d:
            o.content = d['content']
        if 'voucher' in d:
            o.voucher = d['voucher']
        return o


