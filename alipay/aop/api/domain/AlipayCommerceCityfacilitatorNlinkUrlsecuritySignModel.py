#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorNlinkUrlsecuritySignModel(object):

    def __init__(self):
        self._se_uuid = None
        self._tag_id = None

    @property
    def se_uuid(self):
        return self._se_uuid

    @se_uuid.setter
    def se_uuid(self, value):
        self._se_uuid = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.se_uuid:
            if hasattr(self.se_uuid, 'to_alipay_dict'):
                params['se_uuid'] = self.se_uuid.to_alipay_dict()
            else:
                params['se_uuid'] = self.se_uuid
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorNlinkUrlsecuritySignModel()
        if 'se_uuid' in d:
            o.se_uuid = d['se_uuid']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        return o


