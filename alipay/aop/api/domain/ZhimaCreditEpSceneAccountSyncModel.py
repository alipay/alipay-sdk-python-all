#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpSceneAccountSyncModel(object):

    def __init__(self):
        self._biz_no = None
        self._ep_cert_no = None
        self._fail_reason = None
        self._open_status = None
        self._sync_content = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def sync_content(self):
        return self._sync_content

    @sync_content.setter
    def sync_content(self, value):
        if isinstance(value, list):
            self._sync_content = list()
            for i in value:
                self._sync_content.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.open_status:
            if hasattr(self.open_status, 'to_alipay_dict'):
                params['open_status'] = self.open_status.to_alipay_dict()
            else:
                params['open_status'] = self.open_status
        if self.sync_content:
            if isinstance(self.sync_content, list):
                for i in range(0, len(self.sync_content)):
                    element = self.sync_content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sync_content[i] = element.to_alipay_dict()
            if hasattr(self.sync_content, 'to_alipay_dict'):
                params['sync_content'] = self.sync_content.to_alipay_dict()
            else:
                params['sync_content'] = self.sync_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpSceneAccountSyncModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'open_status' in d:
            o.open_status = d['open_status']
        if 'sync_content' in d:
            o.sync_content = d['sync_content']
        return o


