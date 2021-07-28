#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIndirectActivityCopyModel(object):

    def __init__(self):
        self._copy_contents = None
        self._source_smid = None
        self._target_smid = None

    @property
    def copy_contents(self):
        return self._copy_contents

    @copy_contents.setter
    def copy_contents(self, value):
        if isinstance(value, list):
            self._copy_contents = list()
            for i in value:
                self._copy_contents.append(i)
    @property
    def source_smid(self):
        return self._source_smid

    @source_smid.setter
    def source_smid(self, value):
        self._source_smid = value
    @property
    def target_smid(self):
        return self._target_smid

    @target_smid.setter
    def target_smid(self, value):
        self._target_smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.copy_contents:
            if isinstance(self.copy_contents, list):
                for i in range(0, len(self.copy_contents)):
                    element = self.copy_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.copy_contents[i] = element.to_alipay_dict()
            if hasattr(self.copy_contents, 'to_alipay_dict'):
                params['copy_contents'] = self.copy_contents.to_alipay_dict()
            else:
                params['copy_contents'] = self.copy_contents
        if self.source_smid:
            if hasattr(self.source_smid, 'to_alipay_dict'):
                params['source_smid'] = self.source_smid.to_alipay_dict()
            else:
                params['source_smid'] = self.source_smid
        if self.target_smid:
            if hasattr(self.target_smid, 'to_alipay_dict'):
                params['target_smid'] = self.target_smid.to_alipay_dict()
            else:
                params['target_smid'] = self.target_smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectActivityCopyModel()
        if 'copy_contents' in d:
            o.copy_contents = d['copy_contents']
        if 'source_smid' in d:
            o.source_smid = d['source_smid']
        if 'target_smid' in d:
            o.target_smid = d['target_smid']
        return o


