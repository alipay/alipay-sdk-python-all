#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHmUserskipQueryModel(object):

    def __init__(self):
        self._channel = None
        self._equity_code = None
        self._equity_package_code = None
        self._hmuid = None
        self._out_biz_serial_no = None
        self._project_tag = None
        self._tel_no = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def equity_code(self):
        return self._equity_code

    @equity_code.setter
    def equity_code(self, value):
        self._equity_code = value
    @property
    def equity_package_code(self):
        return self._equity_package_code

    @equity_package_code.setter
    def equity_package_code(self, value):
        self._equity_package_code = value
    @property
    def hmuid(self):
        return self._hmuid

    @hmuid.setter
    def hmuid(self, value):
        self._hmuid = value
    @property
    def out_biz_serial_no(self):
        return self._out_biz_serial_no

    @out_biz_serial_no.setter
    def out_biz_serial_no(self, value):
        self._out_biz_serial_no = value
    @property
    def project_tag(self):
        return self._project_tag

    @project_tag.setter
    def project_tag(self, value):
        self._project_tag = value
    @property
    def tel_no(self):
        return self._tel_no

    @tel_no.setter
    def tel_no(self, value):
        self._tel_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.equity_code:
            if hasattr(self.equity_code, 'to_alipay_dict'):
                params['equity_code'] = self.equity_code.to_alipay_dict()
            else:
                params['equity_code'] = self.equity_code
        if self.equity_package_code:
            if hasattr(self.equity_package_code, 'to_alipay_dict'):
                params['equity_package_code'] = self.equity_package_code.to_alipay_dict()
            else:
                params['equity_package_code'] = self.equity_package_code
        if self.hmuid:
            if hasattr(self.hmuid, 'to_alipay_dict'):
                params['hmuid'] = self.hmuid.to_alipay_dict()
            else:
                params['hmuid'] = self.hmuid
        if self.out_biz_serial_no:
            if hasattr(self.out_biz_serial_no, 'to_alipay_dict'):
                params['out_biz_serial_no'] = self.out_biz_serial_no.to_alipay_dict()
            else:
                params['out_biz_serial_no'] = self.out_biz_serial_no
        if self.project_tag:
            if hasattr(self.project_tag, 'to_alipay_dict'):
                params['project_tag'] = self.project_tag.to_alipay_dict()
            else:
                params['project_tag'] = self.project_tag
        if self.tel_no:
            if hasattr(self.tel_no, 'to_alipay_dict'):
                params['tel_no'] = self.tel_no.to_alipay_dict()
            else:
                params['tel_no'] = self.tel_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHmUserskipQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'equity_code' in d:
            o.equity_code = d['equity_code']
        if 'equity_package_code' in d:
            o.equity_package_code = d['equity_package_code']
        if 'hmuid' in d:
            o.hmuid = d['hmuid']
        if 'out_biz_serial_no' in d:
            o.out_biz_serial_no = d['out_biz_serial_no']
        if 'project_tag' in d:
            o.project_tag = d['project_tag']
        if 'tel_no' in d:
            o.tel_no = d['tel_no']
        return o


