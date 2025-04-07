#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftBaseinfoNftidQueryModel(object):

    def __init__(self):
        self._nft_id = None

    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.nft_id:
            if hasattr(self.nft_id, 'to_alipay_dict'):
                params['nft_id'] = self.nft_id.to_alipay_dict()
            else:
                params['nft_id'] = self.nft_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftBaseinfoNftidQueryModel()
        if 'nft_id' in d:
            o.nft_id = d['nft_id']
        return o


