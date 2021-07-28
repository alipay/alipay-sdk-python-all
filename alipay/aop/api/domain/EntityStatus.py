#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EntityStatus(object):

    def __init__(self):
        self._android_can_borrow = None
        self._android_can_borrow_cnt = None
        self._can_borrow = None
        self._can_borrow_cnt = None
        self._can_restore = None
        self._can_restore_cnt = None
        self._ios_can_borrow = None
        self._ios_can_borrow_cnt = None
        self._is_opening = None
        self._typec_can_borrow = None
        self._typec_can_borrow_cnt = None

    @property
    def android_can_borrow(self):
        return self._android_can_borrow

    @android_can_borrow.setter
    def android_can_borrow(self, value):
        self._android_can_borrow = value
    @property
    def android_can_borrow_cnt(self):
        return self._android_can_borrow_cnt

    @android_can_borrow_cnt.setter
    def android_can_borrow_cnt(self, value):
        self._android_can_borrow_cnt = value
    @property
    def can_borrow(self):
        return self._can_borrow

    @can_borrow.setter
    def can_borrow(self, value):
        self._can_borrow = value
    @property
    def can_borrow_cnt(self):
        return self._can_borrow_cnt

    @can_borrow_cnt.setter
    def can_borrow_cnt(self, value):
        self._can_borrow_cnt = value
    @property
    def can_restore(self):
        return self._can_restore

    @can_restore.setter
    def can_restore(self, value):
        self._can_restore = value
    @property
    def can_restore_cnt(self):
        return self._can_restore_cnt

    @can_restore_cnt.setter
    def can_restore_cnt(self, value):
        self._can_restore_cnt = value
    @property
    def ios_can_borrow(self):
        return self._ios_can_borrow

    @ios_can_borrow.setter
    def ios_can_borrow(self, value):
        self._ios_can_borrow = value
    @property
    def ios_can_borrow_cnt(self):
        return self._ios_can_borrow_cnt

    @ios_can_borrow_cnt.setter
    def ios_can_borrow_cnt(self, value):
        self._ios_can_borrow_cnt = value
    @property
    def is_opening(self):
        return self._is_opening

    @is_opening.setter
    def is_opening(self, value):
        self._is_opening = value
    @property
    def typec_can_borrow(self):
        return self._typec_can_borrow

    @typec_can_borrow.setter
    def typec_can_borrow(self, value):
        self._typec_can_borrow = value
    @property
    def typec_can_borrow_cnt(self):
        return self._typec_can_borrow_cnt

    @typec_can_borrow_cnt.setter
    def typec_can_borrow_cnt(self, value):
        self._typec_can_borrow_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.android_can_borrow:
            if hasattr(self.android_can_borrow, 'to_alipay_dict'):
                params['android_can_borrow'] = self.android_can_borrow.to_alipay_dict()
            else:
                params['android_can_borrow'] = self.android_can_borrow
        if self.android_can_borrow_cnt:
            if hasattr(self.android_can_borrow_cnt, 'to_alipay_dict'):
                params['android_can_borrow_cnt'] = self.android_can_borrow_cnt.to_alipay_dict()
            else:
                params['android_can_borrow_cnt'] = self.android_can_borrow_cnt
        if self.can_borrow:
            if hasattr(self.can_borrow, 'to_alipay_dict'):
                params['can_borrow'] = self.can_borrow.to_alipay_dict()
            else:
                params['can_borrow'] = self.can_borrow
        if self.can_borrow_cnt:
            if hasattr(self.can_borrow_cnt, 'to_alipay_dict'):
                params['can_borrow_cnt'] = self.can_borrow_cnt.to_alipay_dict()
            else:
                params['can_borrow_cnt'] = self.can_borrow_cnt
        if self.can_restore:
            if hasattr(self.can_restore, 'to_alipay_dict'):
                params['can_restore'] = self.can_restore.to_alipay_dict()
            else:
                params['can_restore'] = self.can_restore
        if self.can_restore_cnt:
            if hasattr(self.can_restore_cnt, 'to_alipay_dict'):
                params['can_restore_cnt'] = self.can_restore_cnt.to_alipay_dict()
            else:
                params['can_restore_cnt'] = self.can_restore_cnt
        if self.ios_can_borrow:
            if hasattr(self.ios_can_borrow, 'to_alipay_dict'):
                params['ios_can_borrow'] = self.ios_can_borrow.to_alipay_dict()
            else:
                params['ios_can_borrow'] = self.ios_can_borrow
        if self.ios_can_borrow_cnt:
            if hasattr(self.ios_can_borrow_cnt, 'to_alipay_dict'):
                params['ios_can_borrow_cnt'] = self.ios_can_borrow_cnt.to_alipay_dict()
            else:
                params['ios_can_borrow_cnt'] = self.ios_can_borrow_cnt
        if self.is_opening:
            if hasattr(self.is_opening, 'to_alipay_dict'):
                params['is_opening'] = self.is_opening.to_alipay_dict()
            else:
                params['is_opening'] = self.is_opening
        if self.typec_can_borrow:
            if hasattr(self.typec_can_borrow, 'to_alipay_dict'):
                params['typec_can_borrow'] = self.typec_can_borrow.to_alipay_dict()
            else:
                params['typec_can_borrow'] = self.typec_can_borrow
        if self.typec_can_borrow_cnt:
            if hasattr(self.typec_can_borrow_cnt, 'to_alipay_dict'):
                params['typec_can_borrow_cnt'] = self.typec_can_borrow_cnt.to_alipay_dict()
            else:
                params['typec_can_borrow_cnt'] = self.typec_can_borrow_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EntityStatus()
        if 'android_can_borrow' in d:
            o.android_can_borrow = d['android_can_borrow']
        if 'android_can_borrow_cnt' in d:
            o.android_can_borrow_cnt = d['android_can_borrow_cnt']
        if 'can_borrow' in d:
            o.can_borrow = d['can_borrow']
        if 'can_borrow_cnt' in d:
            o.can_borrow_cnt = d['can_borrow_cnt']
        if 'can_restore' in d:
            o.can_restore = d['can_restore']
        if 'can_restore_cnt' in d:
            o.can_restore_cnt = d['can_restore_cnt']
        if 'ios_can_borrow' in d:
            o.ios_can_borrow = d['ios_can_borrow']
        if 'ios_can_borrow_cnt' in d:
            o.ios_can_borrow_cnt = d['ios_can_borrow_cnt']
        if 'is_opening' in d:
            o.is_opening = d['is_opening']
        if 'typec_can_borrow' in d:
            o.typec_can_borrow = d['typec_can_borrow']
        if 'typec_can_borrow_cnt' in d:
            o.typec_can_borrow_cnt = d['typec_can_borrow_cnt']
        return o


