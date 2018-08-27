#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneClaimAttachmentConfirmModel(object):

    def __init__(self):
        self._claim_report_no = None
        self._upload_files = None

    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value
    @property
    def upload_files(self):
        return self._upload_files

    @upload_files.setter
    def upload_files(self, value):
        if isinstance(value, list):
            self._upload_files = list()
            for i in value:
                self._upload_files.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.claim_report_no:
            if hasattr(self.claim_report_no, 'to_alipay_dict'):
                params['claim_report_no'] = self.claim_report_no.to_alipay_dict()
            else:
                params['claim_report_no'] = self.claim_report_no
        if self.upload_files:
            if isinstance(self.upload_files, list):
                for i in range(0, len(self.upload_files)):
                    element = self.upload_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.upload_files[i] = element.to_alipay_dict()
            if hasattr(self.upload_files, 'to_alipay_dict'):
                params['upload_files'] = self.upload_files.to_alipay_dict()
            else:
                params['upload_files'] = self.upload_files
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneClaimAttachmentConfirmModel()
        if 'claim_report_no' in d:
            o.claim_report_no = d['claim_report_no']
        if 'upload_files' in d:
            o.upload_files = d['upload_files']
        return o


