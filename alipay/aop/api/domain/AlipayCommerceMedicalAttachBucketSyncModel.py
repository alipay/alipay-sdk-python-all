#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HdfAttachment import HdfAttachment


class AlipayCommerceMedicalAttachBucketSyncModel(object):

    def __init__(self):
        self._hdf_attachments = None

    @property
    def hdf_attachments(self):
        return self._hdf_attachments

    @hdf_attachments.setter
    def hdf_attachments(self, value):
        if isinstance(value, list):
            self._hdf_attachments = list()
            for i in value:
                if isinstance(i, HdfAttachment):
                    self._hdf_attachments.append(i)
                else:
                    self._hdf_attachments.append(HdfAttachment.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.hdf_attachments:
            if isinstance(self.hdf_attachments, list):
                for i in range(0, len(self.hdf_attachments)):
                    element = self.hdf_attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hdf_attachments[i] = element.to_alipay_dict()
            if hasattr(self.hdf_attachments, 'to_alipay_dict'):
                params['hdf_attachments'] = self.hdf_attachments.to_alipay_dict()
            else:
                params['hdf_attachments'] = self.hdf_attachments
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAttachBucketSyncModel()
        if 'hdf_attachments' in d:
            o.hdf_attachments = d['hdf_attachments']
        return o


