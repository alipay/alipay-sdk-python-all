#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleExtendParams(object):

    def __init__(self):
        self._royalty_finish = None

    @property
    def royalty_finish(self):
        return self._royalty_finish

    @royalty_finish.setter
    def royalty_finish(self, value):
        self._royalty_finish = value


    def to_alipay_dict(self):
        params = dict()
        if self.royalty_finish:
            if hasattr(self.royalty_finish, 'to_alipay_dict'):
                params['royalty_finish'] = self.royalty_finish.to_alipay_dict()
            else:
                params['royalty_finish'] = self.royalty_finish
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleExtendParams()
        if 'royalty_finish' in d:
            o.royalty_finish = d['royalty_finish']
        return o


