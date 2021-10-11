#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaidOuterCardManageUrlConfDTO(object):

    def __init__(self):
        self._cycle_manage_url = None
        self._downgrade_url = None
        self._refund_url = None
        self._renew_url = None
        self._upgrade_url = None

    @property
    def cycle_manage_url(self):
        return self._cycle_manage_url

    @cycle_manage_url.setter
    def cycle_manage_url(self, value):
        self._cycle_manage_url = value
    @property
    def downgrade_url(self):
        return self._downgrade_url

    @downgrade_url.setter
    def downgrade_url(self, value):
        self._downgrade_url = value
    @property
    def refund_url(self):
        return self._refund_url

    @refund_url.setter
    def refund_url(self, value):
        self._refund_url = value
    @property
    def renew_url(self):
        return self._renew_url

    @renew_url.setter
    def renew_url(self, value):
        self._renew_url = value
    @property
    def upgrade_url(self):
        return self._upgrade_url

    @upgrade_url.setter
    def upgrade_url(self, value):
        self._upgrade_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.cycle_manage_url:
            if hasattr(self.cycle_manage_url, 'to_alipay_dict'):
                params['cycle_manage_url'] = self.cycle_manage_url.to_alipay_dict()
            else:
                params['cycle_manage_url'] = self.cycle_manage_url
        if self.downgrade_url:
            if hasattr(self.downgrade_url, 'to_alipay_dict'):
                params['downgrade_url'] = self.downgrade_url.to_alipay_dict()
            else:
                params['downgrade_url'] = self.downgrade_url
        if self.refund_url:
            if hasattr(self.refund_url, 'to_alipay_dict'):
                params['refund_url'] = self.refund_url.to_alipay_dict()
            else:
                params['refund_url'] = self.refund_url
        if self.renew_url:
            if hasattr(self.renew_url, 'to_alipay_dict'):
                params['renew_url'] = self.renew_url.to_alipay_dict()
            else:
                params['renew_url'] = self.renew_url
        if self.upgrade_url:
            if hasattr(self.upgrade_url, 'to_alipay_dict'):
                params['upgrade_url'] = self.upgrade_url.to_alipay_dict()
            else:
                params['upgrade_url'] = self.upgrade_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaidOuterCardManageUrlConfDTO()
        if 'cycle_manage_url' in d:
            o.cycle_manage_url = d['cycle_manage_url']
        if 'downgrade_url' in d:
            o.downgrade_url = d['downgrade_url']
        if 'refund_url' in d:
            o.refund_url = d['refund_url']
        if 'renew_url' in d:
            o.renew_url = d['renew_url']
        if 'upgrade_url' in d:
            o.upgrade_url = d['upgrade_url']
        return o


