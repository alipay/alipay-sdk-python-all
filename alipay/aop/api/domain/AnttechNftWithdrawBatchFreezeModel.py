#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftWithdrawBatchFreezeModel(object):

    def __init__(self):
        self._biz_id = None
        self._id_no = None
        self._id_type = None
        self._nft_id_set = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def id_no(self):
        return self._id_no

    @id_no.setter
    def id_no(self, value):
        self._id_no = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def nft_id_set(self):
        return self._nft_id_set

    @nft_id_set.setter
    def nft_id_set(self, value):
        if isinstance(value, list):
            self._nft_id_set = list()
            for i in value:
                self._nft_id_set.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.id_no:
            if hasattr(self.id_no, 'to_alipay_dict'):
                params['id_no'] = self.id_no.to_alipay_dict()
            else:
                params['id_no'] = self.id_no
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.nft_id_set:
            if isinstance(self.nft_id_set, list):
                for i in range(0, len(self.nft_id_set)):
                    element = self.nft_id_set[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.nft_id_set[i] = element.to_alipay_dict()
            if hasattr(self.nft_id_set, 'to_alipay_dict'):
                params['nft_id_set'] = self.nft_id_set.to_alipay_dict()
            else:
                params['nft_id_set'] = self.nft_id_set
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftWithdrawBatchFreezeModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'id_no' in d:
            o.id_no = d['id_no']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'nft_id_set' in d:
            o.nft_id_set = d['nft_id_set']
        return o


