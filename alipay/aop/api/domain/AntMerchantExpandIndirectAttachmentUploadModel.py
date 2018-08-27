#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttachmentInfo import AttachmentInfo


class AntMerchantExpandIndirectAttachmentUploadModel(object):

    def __init__(self):
        self._attachment_info = None
        self._memo = None
        self._sub_merchant_id = None

    @property
    def attachment_info(self):
        return self._attachment_info

    @attachment_info.setter
    def attachment_info(self, value):
        if isinstance(value, list):
            self._attachment_info = list()
            for i in value:
                if isinstance(i, AttachmentInfo):
                    self._attachment_info.append(i)
                else:
                    self._attachment_info.append(AttachmentInfo.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_info:
            if isinstance(self.attachment_info, list):
                for i in range(0, len(self.attachment_info)):
                    element = self.attachment_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachment_info[i] = element.to_alipay_dict()
            if hasattr(self.attachment_info, 'to_alipay_dict'):
                params['attachment_info'] = self.attachment_info.to_alipay_dict()
            else:
                params['attachment_info'] = self.attachment_info
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectAttachmentUploadModel()
        if 'attachment_info' in d:
            o.attachment_info = d['attachment_info']
        if 'memo' in d:
            o.memo = d['memo']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        return o


