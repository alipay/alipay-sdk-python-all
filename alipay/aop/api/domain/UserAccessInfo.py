#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserSegmentationInfo import UserSegmentationInfo


class UserAccessInfo(object):

    def __init__(self):
        self._tel_num = None
        self._user_segmentation_info = None

    @property
    def tel_num(self):
        return self._tel_num

    @tel_num.setter
    def tel_num(self, value):
        self._tel_num = value
    @property
    def user_segmentation_info(self):
        return self._user_segmentation_info

    @user_segmentation_info.setter
    def user_segmentation_info(self, value):
        if isinstance(value, list):
            self._user_segmentation_info = list()
            for i in value:
                if isinstance(i, UserSegmentationInfo):
                    self._user_segmentation_info.append(i)
                else:
                    self._user_segmentation_info.append(UserSegmentationInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.tel_num:
            if hasattr(self.tel_num, 'to_alipay_dict'):
                params['tel_num'] = self.tel_num.to_alipay_dict()
            else:
                params['tel_num'] = self.tel_num
        if self.user_segmentation_info:
            if isinstance(self.user_segmentation_info, list):
                for i in range(0, len(self.user_segmentation_info)):
                    element = self.user_segmentation_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_segmentation_info[i] = element.to_alipay_dict()
            if hasattr(self.user_segmentation_info, 'to_alipay_dict'):
                params['user_segmentation_info'] = self.user_segmentation_info.to_alipay_dict()
            else:
                params['user_segmentation_info'] = self.user_segmentation_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserAccessInfo()
        if 'tel_num' in d:
            o.tel_num = d['tel_num']
        if 'user_segmentation_info' in d:
            o.user_segmentation_info = d['user_segmentation_info']
        return o


