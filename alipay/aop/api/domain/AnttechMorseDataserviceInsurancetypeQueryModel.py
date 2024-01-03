#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseDataserviceInsurancetypeQueryModel(object):

    def __init__(self):
        self._id_card_sha_256 = None

    @property
    def id_card_sha_256(self):
        return self._id_card_sha_256

    @id_card_sha_256.setter
    def id_card_sha_256(self, value):
        self._id_card_sha_256 = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_card_sha_256:
            if hasattr(self.id_card_sha_256, 'to_alipay_dict'):
                params['id_card_sha_256'] = self.id_card_sha_256.to_alipay_dict()
            else:
                params['id_card_sha_256'] = self.id_card_sha_256
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseDataserviceInsurancetypeQueryModel()
        if 'id_card_sha_256' in d:
            o.id_card_sha_256 = d['id_card_sha_256']
        return o


