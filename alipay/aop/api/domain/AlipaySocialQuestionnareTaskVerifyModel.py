#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialQuestionnareTaskVerifyModel(object):

    def __init__(self):
        self._buyer_user_ids = None
        self._ext_info = None
        self._qstn_id = None
        self._rmt_qstn_id = None

    @property
    def buyer_user_ids(self):
        return self._buyer_user_ids

    @buyer_user_ids.setter
    def buyer_user_ids(self, value):
        self._buyer_user_ids = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
        if self.buyer_user_ids:
            if hasattr(self.buyer_user_ids, 'to_alipay_dict'):
                params['buyer_user_ids'] = self.buyer_user_ids.to_alipay_dict()
            else:
                params['buyer_user_ids'] = self.buyer_user_ids
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        o = AlipaySocialQuestionnareTaskVerifyModel()
        if 'buyer_user_ids' in d:
            o.buyer_user_ids = d['buyer_user_ids']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'qstn_id' in d:
            o.qstn_id = d['qstn_id']
        if 'rmt_qstn_id' in d:
            o.rmt_qstn_id = d['rmt_qstn_id']
        return o


