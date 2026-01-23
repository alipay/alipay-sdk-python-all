#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandFileInfoOpenApi import BrandFileInfoOpenApi
from alipay.aop.api.domain.BrandFileInfoOpenApi import BrandFileInfoOpenApi
from alipay.aop.api.domain.BrandFileInfoOpenApi import BrandFileInfoOpenApi
from alipay.aop.api.domain.BrandFileInfoOpenApi import BrandFileInfoOpenApi


class BrandAuthMaterialInfoOpenApi(object):

    def __init__(self):
        self._auth_level = None
        self._belong_person = None
        self._brand_manage_type = None
        self._brand_relation_proof = None
        self._id_card_file = None
        self._passport = None
        self._person_certification = None
        self._qualifications = None

    @property
    def auth_level(self):
        return self._auth_level

    @auth_level.setter
    def auth_level(self, value):
        self._auth_level = value
    @property
    def belong_person(self):
        return self._belong_person

    @belong_person.setter
    def belong_person(self, value):
        self._belong_person = value
    @property
    def brand_manage_type(self):
        return self._brand_manage_type

    @brand_manage_type.setter
    def brand_manage_type(self, value):
        self._brand_manage_type = value
    @property
    def brand_relation_proof(self):
        return self._brand_relation_proof

    @brand_relation_proof.setter
    def brand_relation_proof(self, value):
        if isinstance(value, list):
            self._brand_relation_proof = list()
            for i in value:
                if isinstance(i, BrandFileInfoOpenApi):
                    self._brand_relation_proof.append(i)
                else:
                    self._brand_relation_proof.append(BrandFileInfoOpenApi.from_alipay_dict(i))
    @property
    def id_card_file(self):
        return self._id_card_file

    @id_card_file.setter
    def id_card_file(self, value):
        if isinstance(value, list):
            self._id_card_file = list()
            for i in value:
                if isinstance(i, BrandFileInfoOpenApi):
                    self._id_card_file.append(i)
                else:
                    self._id_card_file.append(BrandFileInfoOpenApi.from_alipay_dict(i))
    @property
    def passport(self):
        return self._passport

    @passport.setter
    def passport(self, value):
        if isinstance(value, list):
            self._passport = list()
            for i in value:
                if isinstance(i, BrandFileInfoOpenApi):
                    self._passport.append(i)
                else:
                    self._passport.append(BrandFileInfoOpenApi.from_alipay_dict(i))
    @property
    def person_certification(self):
        return self._person_certification

    @person_certification.setter
    def person_certification(self, value):
        self._person_certification = value
    @property
    def qualifications(self):
        return self._qualifications

    @qualifications.setter
    def qualifications(self, value):
        if isinstance(value, list):
            self._qualifications = list()
            for i in value:
                if isinstance(i, BrandFileInfoOpenApi):
                    self._qualifications.append(i)
                else:
                    self._qualifications.append(BrandFileInfoOpenApi.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.auth_level:
            if hasattr(self.auth_level, 'to_alipay_dict'):
                params['auth_level'] = self.auth_level.to_alipay_dict()
            else:
                params['auth_level'] = self.auth_level
        if self.belong_person:
            if hasattr(self.belong_person, 'to_alipay_dict'):
                params['belong_person'] = self.belong_person.to_alipay_dict()
            else:
                params['belong_person'] = self.belong_person
        if self.brand_manage_type:
            if hasattr(self.brand_manage_type, 'to_alipay_dict'):
                params['brand_manage_type'] = self.brand_manage_type.to_alipay_dict()
            else:
                params['brand_manage_type'] = self.brand_manage_type
        if self.brand_relation_proof:
            if isinstance(self.brand_relation_proof, list):
                for i in range(0, len(self.brand_relation_proof)):
                    element = self.brand_relation_proof[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_relation_proof[i] = element.to_alipay_dict()
            if hasattr(self.brand_relation_proof, 'to_alipay_dict'):
                params['brand_relation_proof'] = self.brand_relation_proof.to_alipay_dict()
            else:
                params['brand_relation_proof'] = self.brand_relation_proof
        if self.id_card_file:
            if isinstance(self.id_card_file, list):
                for i in range(0, len(self.id_card_file)):
                    element = self.id_card_file[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.id_card_file[i] = element.to_alipay_dict()
            if hasattr(self.id_card_file, 'to_alipay_dict'):
                params['id_card_file'] = self.id_card_file.to_alipay_dict()
            else:
                params['id_card_file'] = self.id_card_file
        if self.passport:
            if isinstance(self.passport, list):
                for i in range(0, len(self.passport)):
                    element = self.passport[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.passport[i] = element.to_alipay_dict()
            if hasattr(self.passport, 'to_alipay_dict'):
                params['passport'] = self.passport.to_alipay_dict()
            else:
                params['passport'] = self.passport
        if self.person_certification:
            if hasattr(self.person_certification, 'to_alipay_dict'):
                params['person_certification'] = self.person_certification.to_alipay_dict()
            else:
                params['person_certification'] = self.person_certification
        if self.qualifications:
            if isinstance(self.qualifications, list):
                for i in range(0, len(self.qualifications)):
                    element = self.qualifications[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qualifications[i] = element.to_alipay_dict()
            if hasattr(self.qualifications, 'to_alipay_dict'):
                params['qualifications'] = self.qualifications.to_alipay_dict()
            else:
                params['qualifications'] = self.qualifications
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandAuthMaterialInfoOpenApi()
        if 'auth_level' in d:
            o.auth_level = d['auth_level']
        if 'belong_person' in d:
            o.belong_person = d['belong_person']
        if 'brand_manage_type' in d:
            o.brand_manage_type = d['brand_manage_type']
        if 'brand_relation_proof' in d:
            o.brand_relation_proof = d['brand_relation_proof']
        if 'id_card_file' in d:
            o.id_card_file = d['id_card_file']
        if 'passport' in d:
            o.passport = d['passport']
        if 'person_certification' in d:
            o.person_certification = d['person_certification']
        if 'qualifications' in d:
            o.qualifications = d['qualifications']
        return o


