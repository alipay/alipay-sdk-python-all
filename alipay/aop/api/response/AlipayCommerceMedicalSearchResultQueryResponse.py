#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ArticleVo import ArticleVo
from alipay.aop.api.domain.SimpleDoctorInfo import SimpleDoctorInfo
from alipay.aop.api.domain.SimpleHospitalInfo import SimpleHospitalInfo
from alipay.aop.api.domain.KeyInfo import KeyInfo
from alipay.aop.api.domain.MedicalRecordVo import MedicalRecordVo
from alipay.aop.api.domain.Term import Term


class AlipayCommerceMedicalSearchResultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalSearchResultQueryResponse, self).__init__()
        self._activity_list = None
        self._article_list = None
        self._doctor_info_list = None
        self._has_more = None
        self._hospital_list = None
        self._key_list = None
        self._medical_record_list = None
        self._sort_list = None
        self._term_list = None

    @property
    def activity_list(self):
        return self._activity_list

    @activity_list.setter
    def activity_list(self, value):
        self._activity_list = value
    @property
    def article_list(self):
        return self._article_list

    @article_list.setter
    def article_list(self, value):
        if isinstance(value, ArticleVo):
            self._article_list = value
        else:
            self._article_list = ArticleVo.from_alipay_dict(value)
    @property
    def doctor_info_list(self):
        return self._doctor_info_list

    @doctor_info_list.setter
    def doctor_info_list(self, value):
        if isinstance(value, SimpleDoctorInfo):
            self._doctor_info_list = value
        else:
            self._doctor_info_list = SimpleDoctorInfo.from_alipay_dict(value)
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def hospital_list(self):
        return self._hospital_list

    @hospital_list.setter
    def hospital_list(self, value):
        if isinstance(value, SimpleHospitalInfo):
            self._hospital_list = value
        else:
            self._hospital_list = SimpleHospitalInfo.from_alipay_dict(value)
    @property
    def key_list(self):
        return self._key_list

    @key_list.setter
    def key_list(self, value):
        if isinstance(value, KeyInfo):
            self._key_list = value
        else:
            self._key_list = KeyInfo.from_alipay_dict(value)
    @property
    def medical_record_list(self):
        return self._medical_record_list

    @medical_record_list.setter
    def medical_record_list(self, value):
        if isinstance(value, MedicalRecordVo):
            self._medical_record_list = value
        else:
            self._medical_record_list = MedicalRecordVo.from_alipay_dict(value)
    @property
    def sort_list(self):
        return self._sort_list

    @sort_list.setter
    def sort_list(self, value):
        if isinstance(value, list):
            self._sort_list = list()
            for i in value:
                self._sort_list.append(i)
    @property
    def term_list(self):
        return self._term_list

    @term_list.setter
    def term_list(self, value):
        if isinstance(value, Term):
            self._term_list = value
        else:
            self._term_list = Term.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalSearchResultQueryResponse, self).parse_response_content(response_content)
        if 'activity_list' in response:
            self.activity_list = response['activity_list']
        if 'article_list' in response:
            self.article_list = response['article_list']
        if 'doctor_info_list' in response:
            self.doctor_info_list = response['doctor_info_list']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'hospital_list' in response:
            self.hospital_list = response['hospital_list']
        if 'key_list' in response:
            self.key_list = response['key_list']
        if 'medical_record_list' in response:
            self.medical_record_list = response['medical_record_list']
        if 'sort_list' in response:
            self.sort_list = response['sort_list']
        if 'term_list' in response:
            self.term_list = response['term_list']
