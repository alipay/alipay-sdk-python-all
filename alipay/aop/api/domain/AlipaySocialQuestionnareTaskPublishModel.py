#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialQuestionnareTaskPublishModel(object):

    def __init__(self):
        self._biz_channel = None
        self._ext_info = None
        self._out_request_no = None
        self._qstn_id = None
        self._rmt_qstn_id = None

    @property
    def biz_channel(self):
        return self._biz_channel

    @biz_channel.setter
    def biz_channel(self, value):
        self._biz_channel = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def qstn_id(self):
        return self._qstn_id

    @qstn_id.setter
    def qstn_id(self, value):
        self._qstn_id = value
    @property
    def rmt_qstn_id(self):
        return self._rmt_qstn_id

    @rmt_qstn_id.setter
    def rmt_qstn_id(self, value):
        self._rmt_qstn_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_channel:
            if hasattr(self.biz_channel, 'to_alipay_dict'):
                params['biz_channel'] = self.biz_channel.to_alipay_dict()
            else:
                params['biz_channel'] = self.biz_channel
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.qstn_id:
            if hasattr(self.qstn_id, 'to_alipay_dict'):
                params['qstn_id'] = self.qstn_id.to_alipay_dict()
            else:
                params['qstn_id'] = self.qstn_id
        if self.rmt_qstn_id:
            if hasattr(self.rmt_qstn_id, 'to_alipay_dict'):
                params['rmt_qstn_id'] = self.rmt_qstn_id.to_alipay_dict()
            else:
                params['rmt_qstn_id'] = self.rmt_qstn_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialQuestionnareTaskPublishModel()
        if 'biz_channel' in d:
            o.biz_channel = d['biz_channel']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'qstn_id' in d:
            o.qstn_id = d['qstn_id']
        if 'rmt_qstn_id' in d:
            o.rmt_qstn_id = d['rmt_qstn_id']
        return o


