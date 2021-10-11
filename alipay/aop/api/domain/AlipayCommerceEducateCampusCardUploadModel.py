#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CampusCardPicture import CampusCardPicture


class AlipayCommerceEducateCampusCardUploadModel(object):

    def __init__(self):
        self._biz_source_from = None
        self._campus_card_picture = None
        self._card_pictures = None
        self._degree = None
        self._enroll_date = None
        self._school_name = None

    @property
    def biz_source_from(self):
        return self._biz_source_from

    @biz_source_from.setter
    def biz_source_from(self, value):
        self._biz_source_from = value
    @property
    def campus_card_picture(self):
        return self._campus_card_picture

    @campus_card_picture.setter
    def campus_card_picture(self, value):
        if isinstance(value, list):
            self._campus_card_picture = list()
            for i in value:
                self._campus_card_picture.append(i)
    @property
    def card_pictures(self):
        return self._card_pictures

    @card_pictures.setter
    def card_pictures(self, value):
        if isinstance(value, list):
            self._card_pictures = list()
            for i in value:
                if isinstance(i, CampusCardPicture):
                    self._card_pictures.append(i)
                else:
                    self._card_pictures.append(CampusCardPicture.from_alipay_dict(i))
    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        self._degree = value
    @property
    def enroll_date(self):
        return self._enroll_date

    @enroll_date.setter
    def enroll_date(self, value):
        self._enroll_date = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source_from:
            if hasattr(self.biz_source_from, 'to_alipay_dict'):
                params['biz_source_from'] = self.biz_source_from.to_alipay_dict()
            else:
                params['biz_source_from'] = self.biz_source_from
        if self.campus_card_picture:
            if isinstance(self.campus_card_picture, list):
                for i in range(0, len(self.campus_card_picture)):
                    element = self.campus_card_picture[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.campus_card_picture[i] = element.to_alipay_dict()
            if hasattr(self.campus_card_picture, 'to_alipay_dict'):
                params['campus_card_picture'] = self.campus_card_picture.to_alipay_dict()
            else:
                params['campus_card_picture'] = self.campus_card_picture
        if self.card_pictures:
            if isinstance(self.card_pictures, list):
                for i in range(0, len(self.card_pictures)):
                    element = self.card_pictures[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_pictures[i] = element.to_alipay_dict()
            if hasattr(self.card_pictures, 'to_alipay_dict'):
                params['card_pictures'] = self.card_pictures.to_alipay_dict()
            else:
                params['card_pictures'] = self.card_pictures
        if self.degree:
            if hasattr(self.degree, 'to_alipay_dict'):
                params['degree'] = self.degree.to_alipay_dict()
            else:
                params['degree'] = self.degree
        if self.enroll_date:
            if hasattr(self.enroll_date, 'to_alipay_dict'):
                params['enroll_date'] = self.enroll_date.to_alipay_dict()
            else:
                params['enroll_date'] = self.enroll_date
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateCampusCardUploadModel()
        if 'biz_source_from' in d:
            o.biz_source_from = d['biz_source_from']
        if 'campus_card_picture' in d:
            o.campus_card_picture = d['campus_card_picture']
        if 'card_pictures' in d:
            o.card_pictures = d['card_pictures']
        if 'degree' in d:
            o.degree = d['degree']
        if 'enroll_date' in d:
            o.enroll_date = d['enroll_date']
        if 'school_name' in d:
            o.school_name = d['school_name']
        return o


