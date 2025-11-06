#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UniOpenResItemDetailInfos import UniOpenResItemDetailInfos


class UniOpenResItem(object):

    def __init__(self):
        self._detail_infos = None
        self._fail_reason = None
        self._open_type = None
        self._status = None

    @property
    def detail_infos(self):
        return self._detail_infos

    @detail_infos.setter
    def detail_infos(self, value):
        if isinstance(value, UniOpenResItemDetailInfos):
            self._detail_infos = value
        else:
            self._detail_infos = UniOpenResItemDetailInfos.from_alipay_dict(value)
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def open_type(self):
        return self._open_type

    @open_type.setter
    def open_type(self, value):
        self._open_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_infos:
            if hasattr(self.detail_infos, 'to_alipay_dict'):
                params['detail_infos'] = self.detail_infos.to_alipay_dict()
            else:
                params['detail_infos'] = self.detail_infos
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.open_type:
            if hasattr(self.open_type, 'to_alipay_dict'):
                params['open_type'] = self.open_type.to_alipay_dict()
            else:
                params['open_type'] = self.open_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UniOpenResItem()
        if 'detail_infos' in d:
            o.detail_infos = d['detail_infos']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'open_type' in d:
            o.open_type = d['open_type']
        if 'status' in d:
            o.status = d['status']
        return o


