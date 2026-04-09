#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FreigtFlowSpdbBizSeqNo(object):

    def __init__(self):
        self._channel_seq_no = None
        self._tran_seq_no = None
        self._ylk_tran_seq_no = None

    @property
    def channel_seq_no(self):
        return self._channel_seq_no

    @channel_seq_no.setter
    def channel_seq_no(self, value):
        self._channel_seq_no = value
    @property
    def tran_seq_no(self):
        return self._tran_seq_no

    @tran_seq_no.setter
    def tran_seq_no(self, value):
        self._tran_seq_no = value
    @property
    def ylk_tran_seq_no(self):
        return self._ylk_tran_seq_no

    @ylk_tran_seq_no.setter
    def ylk_tran_seq_no(self, value):
        self._ylk_tran_seq_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_seq_no:
            if hasattr(self.channel_seq_no, 'to_alipay_dict'):
                params['channel_seq_no'] = self.channel_seq_no.to_alipay_dict()
            else:
                params['channel_seq_no'] = self.channel_seq_no
        if self.tran_seq_no:
            if hasattr(self.tran_seq_no, 'to_alipay_dict'):
                params['tran_seq_no'] = self.tran_seq_no.to_alipay_dict()
            else:
                params['tran_seq_no'] = self.tran_seq_no
        if self.ylk_tran_seq_no:
            if hasattr(self.ylk_tran_seq_no, 'to_alipay_dict'):
                params['ylk_tran_seq_no'] = self.ylk_tran_seq_no.to_alipay_dict()
            else:
                params['ylk_tran_seq_no'] = self.ylk_tran_seq_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FreigtFlowSpdbBizSeqNo()
        if 'channel_seq_no' in d:
            o.channel_seq_no = d['channel_seq_no']
        if 'tran_seq_no' in d:
            o.tran_seq_no = d['tran_seq_no']
        if 'ylk_tran_seq_no' in d:
            o.ylk_tran_seq_no = d['ylk_tran_seq_no']
        return o


