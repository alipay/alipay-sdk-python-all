#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CloudResumeCertificateInfo import CloudResumeCertificateInfo
from alipay.aop.api.domain.CloudResumeEducationExperience import CloudResumeEducationExperience
from alipay.aop.api.domain.CloudResumeHeadPic import CloudResumeHeadPic
from alipay.aop.api.domain.CloudResumePositionIntention import CloudResumePositionIntention
from alipay.aop.api.domain.CloudResumeSkillInfo import CloudResumeSkillInfo
from alipay.aop.api.domain.CloudResumeWorkExperience import CloudResumeWorkExperience


class ZhimaCustomerJobworthCloudresumeQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerJobworthCloudresumeQueryResponse, self).__init__()
        self._birthday = None
        self._certificates = None
        self._education_experiences = None
        self._email = None
        self._gender = None
        self._intention_status = None
        self._person_desc = None
        self._phone = None
        self._pic_url = None
        self._position_intentions = None
        self._position_type = None
        self._residential_area = None
        self._skills = None
        self._user_name = None
        self._work_experiences = None
        self._work_start_date = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def certificates(self):
        return self._certificates

    @certificates.setter
    def certificates(self, value):
        if isinstance(value, list):
            self._certificates = list()
            for i in value:
                if isinstance(i, CloudResumeCertificateInfo):
                    self._certificates.append(i)
                else:
                    self._certificates.append(CloudResumeCertificateInfo.from_alipay_dict(i))
    @property
    def education_experiences(self):
        return self._education_experiences

    @education_experiences.setter
    def education_experiences(self, value):
        if isinstance(value, list):
            self._education_experiences = list()
            for i in value:
                if isinstance(i, CloudResumeEducationExperience):
                    self._education_experiences.append(i)
                else:
                    self._education_experiences.append(CloudResumeEducationExperience.from_alipay_dict(i))
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def intention_status(self):
        return self._intention_status

    @intention_status.setter
    def intention_status(self, value):
        self._intention_status = value
    @property
    def person_desc(self):
        return self._person_desc

    @person_desc.setter
    def person_desc(self, value):
        self._person_desc = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        if isinstance(value, CloudResumeHeadPic):
            self._pic_url = value
        else:
            self._pic_url = CloudResumeHeadPic.from_alipay_dict(value)
    @property
    def position_intentions(self):
        return self._position_intentions

    @position_intentions.setter
    def position_intentions(self, value):
        if isinstance(value, list):
            self._position_intentions = list()
            for i in value:
                if isinstance(i, CloudResumePositionIntention):
                    self._position_intentions.append(i)
                else:
                    self._position_intentions.append(CloudResumePositionIntention.from_alipay_dict(i))
    @property
    def position_type(self):
        return self._position_type

    @position_type.setter
    def position_type(self, value):
        self._position_type = value
    @property
    def residential_area(self):
        return self._residential_area

    @residential_area.setter
    def residential_area(self, value):
        self._residential_area = value
    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, value):
        if isinstance(value, list):
            self._skills = list()
            for i in value:
                if isinstance(i, CloudResumeSkillInfo):
                    self._skills.append(i)
                else:
                    self._skills.append(CloudResumeSkillInfo.from_alipay_dict(i))
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def work_experiences(self):
        return self._work_experiences

    @work_experiences.setter
    def work_experiences(self, value):
        if isinstance(value, list):
            self._work_experiences = list()
            for i in value:
                if isinstance(i, CloudResumeWorkExperience):
                    self._work_experiences.append(i)
                else:
                    self._work_experiences.append(CloudResumeWorkExperience.from_alipay_dict(i))
    @property
    def work_start_date(self):
        return self._work_start_date

    @work_start_date.setter
    def work_start_date(self, value):
        self._work_start_date = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerJobworthCloudresumeQueryResponse, self).parse_response_content(response_content)
        if 'birthday' in response:
            self.birthday = response['birthday']
        if 'certificates' in response:
            self.certificates = response['certificates']
        if 'education_experiences' in response:
            self.education_experiences = response['education_experiences']
        if 'email' in response:
            self.email = response['email']
        if 'gender' in response:
            self.gender = response['gender']
        if 'intention_status' in response:
            self.intention_status = response['intention_status']
        if 'person_desc' in response:
            self.person_desc = response['person_desc']
        if 'phone' in response:
            self.phone = response['phone']
        if 'pic_url' in response:
            self.pic_url = response['pic_url']
        if 'position_intentions' in response:
            self.position_intentions = response['position_intentions']
        if 'position_type' in response:
            self.position_type = response['position_type']
        if 'residential_area' in response:
            self.residential_area = response['residential_area']
        if 'skills' in response:
            self.skills = response['skills']
        if 'user_name' in response:
            self.user_name = response['user_name']
        if 'work_experiences' in response:
            self.work_experiences = response['work_experiences']
        if 'work_start_date' in response:
            self.work_start_date = response['work_start_date']
