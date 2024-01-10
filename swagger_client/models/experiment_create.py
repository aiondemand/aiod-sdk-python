# coding: utf-8

"""
    FastAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExperimentCreate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'platform': 'object',
        'platform_resource_identifier': 'object',
        'name': 'object',
        'date_published': 'object',
        'same_as': 'object',
        'is_accessible_for_free': 'object',
        'version': 'object',
        'pid': 'object',
        'experimental_workflow': 'object',
        'execution_settings': 'object',
        'reproducibility_explanation': 'object',
        'aiod_entry': 'AIoDEntryCreate',
        'alternate_name': 'object',
        'application_area': 'object',
        'badge': 'object',
        'citation': 'object',
        'contact': 'object',
        'creator': 'object',
        'description': 'Text',
        'distribution': 'object',
        'has_part': 'object',
        'industrial_sector': 'object',
        'is_part_of': 'object',
        'keyword': 'object',
        'license': 'object',
        'media': 'object',
        'note': 'object',
        'relevant_link': 'object',
        'relevant_resource': 'object',
        'relevant_to': 'object',
        'research_area': 'object',
        'scientific_domain': 'object'
    }

    attribute_map = {
        'platform': 'platform',
        'platform_resource_identifier': 'platform_resource_identifier',
        'name': 'name',
        'date_published': 'date_published',
        'same_as': 'same_as',
        'is_accessible_for_free': 'is_accessible_for_free',
        'version': 'version',
        'pid': 'pid',
        'experimental_workflow': 'experimental_workflow',
        'execution_settings': 'execution_settings',
        'reproducibility_explanation': 'reproducibility_explanation',
        'aiod_entry': 'aiod_entry',
        'alternate_name': 'alternate_name',
        'application_area': 'application_area',
        'badge': 'badge',
        'citation': 'citation',
        'contact': 'contact',
        'creator': 'creator',
        'description': 'description',
        'distribution': 'distribution',
        'has_part': 'has_part',
        'industrial_sector': 'industrial_sector',
        'is_part_of': 'is_part_of',
        'keyword': 'keyword',
        'license': 'license',
        'media': 'media',
        'note': 'note',
        'relevant_link': 'relevant_link',
        'relevant_resource': 'relevant_resource',
        'relevant_to': 'relevant_to',
        'research_area': 'research_area',
        'scientific_domain': 'scientific_domain'
    }

    def __init__(self, platform=None, platform_resource_identifier=None, name=None, date_published=None, same_as=None, is_accessible_for_free=None, version=None, pid=None, experimental_workflow=None, execution_settings=None, reproducibility_explanation=None, aiod_entry=None, alternate_name=None, application_area=None, badge=None, citation=None, contact=None, creator=None, description=None, distribution=None, has_part=None, industrial_sector=None, is_part_of=None, keyword=None, license=None, media=None, note=None, relevant_link=None, relevant_resource=None, relevant_to=None, research_area=None, scientific_domain=None):  # noqa: E501
        """ExperimentCreate - a model defined in Swagger"""  # noqa: E501
        self._platform = None
        self._platform_resource_identifier = None
        self._name = None
        self._date_published = None
        self._same_as = None
        self._is_accessible_for_free = None
        self._version = None
        self._pid = None
        self._experimental_workflow = None
        self._execution_settings = None
        self._reproducibility_explanation = None
        self._aiod_entry = None
        self._alternate_name = None
        self._application_area = None
        self._badge = None
        self._citation = None
        self._contact = None
        self._creator = None
        self._description = None
        self._distribution = None
        self._has_part = None
        self._industrial_sector = None
        self._is_part_of = None
        self._keyword = None
        self._license = None
        self._media = None
        self._note = None
        self._relevant_link = None
        self._relevant_resource = None
        self._relevant_to = None
        self._research_area = None
        self._scientific_domain = None
        self.discriminator = None
        if platform is not None:
            self.platform = platform
        if platform_resource_identifier is not None:
            self.platform_resource_identifier = platform_resource_identifier
        self.name = name
        if date_published is not None:
            self.date_published = date_published
        if same_as is not None:
            self.same_as = same_as
        if is_accessible_for_free is not None:
            self.is_accessible_for_free = is_accessible_for_free
        if version is not None:
            self.version = version
        if pid is not None:
            self.pid = pid
        if experimental_workflow is not None:
            self.experimental_workflow = experimental_workflow
        if execution_settings is not None:
            self.execution_settings = execution_settings
        if reproducibility_explanation is not None:
            self.reproducibility_explanation = reproducibility_explanation
        if aiod_entry is not None:
            self.aiod_entry = aiod_entry
        if alternate_name is not None:
            self.alternate_name = alternate_name
        if application_area is not None:
            self.application_area = application_area
        if badge is not None:
            self.badge = badge
        if citation is not None:
            self.citation = citation
        if contact is not None:
            self.contact = contact
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if distribution is not None:
            self.distribution = distribution
        if has_part is not None:
            self.has_part = has_part
        if industrial_sector is not None:
            self.industrial_sector = industrial_sector
        if is_part_of is not None:
            self.is_part_of = is_part_of
        if keyword is not None:
            self.keyword = keyword
        if license is not None:
            self.license = license
        if media is not None:
            self.media = media
        if note is not None:
            self.note = note
        if relevant_link is not None:
            self.relevant_link = relevant_link
        if relevant_resource is not None:
            self.relevant_resource = relevant_resource
        if relevant_to is not None:
            self.relevant_to = relevant_to
        if research_area is not None:
            self.research_area = research_area
        if scientific_domain is not None:
            self.scientific_domain = scientific_domain

    @property
    def platform(self):
        """Gets the platform of this ExperimentCreate.  # noqa: E501

        The external platform from which this resource originates. Leave empty if this item originates from AIoD. If platform is not None, the platform_resource_identifier should be set as well.  # noqa: E501

        :return: The platform of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ExperimentCreate.

        The external platform from which this resource originates. Leave empty if this item originates from AIoD. If platform is not None, the platform_resource_identifier should be set as well.  # noqa: E501

        :param platform: The platform of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._platform = platform

    @property
    def platform_resource_identifier(self):
        """Gets the platform_resource_identifier of this ExperimentCreate.  # noqa: E501

        A unique identifier issued by the external platform that's specified in 'platform'. Leave empty if this item is not part of an external platform.  # noqa: E501

        :return: The platform_resource_identifier of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._platform_resource_identifier

    @platform_resource_identifier.setter
    def platform_resource_identifier(self, platform_resource_identifier):
        """Sets the platform_resource_identifier of this ExperimentCreate.

        A unique identifier issued by the external platform that's specified in 'platform'. Leave empty if this item is not part of an external platform.  # noqa: E501

        :param platform_resource_identifier: The platform_resource_identifier of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._platform_resource_identifier = platform_resource_identifier

    @property
    def name(self):
        """Gets the name of this ExperimentCreate.  # noqa: E501


        :return: The name of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExperimentCreate.


        :param name: The name of this ExperimentCreate.  # noqa: E501
        :type: object
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def date_published(self):
        """Gets the date_published of this ExperimentCreate.  # noqa: E501

        The datetime (utc) on which this resource was first published on an external platform. Note the difference between `.aiod_entry.date_created` and `.date_published`: the former is automatically set to the datetime the resource was created on AIoD, while the latter can optionally be set to an earlier datetime that the resource was published on an external platform.  # noqa: E501

        :return: The date_published of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this ExperimentCreate.

        The datetime (utc) on which this resource was first published on an external platform. Note the difference between `.aiod_entry.date_created` and `.date_published`: the former is automatically set to the datetime the resource was created on AIoD, while the latter can optionally be set to an earlier datetime that the resource was published on an external platform.  # noqa: E501

        :param date_published: The date_published of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._date_published = date_published

    @property
    def same_as(self):
        """Gets the same_as of this ExperimentCreate.  # noqa: E501

        Url of a reference Web page that unambiguously indicates this resource's identity.  # noqa: E501

        :return: The same_as of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._same_as

    @same_as.setter
    def same_as(self, same_as):
        """Sets the same_as of this ExperimentCreate.

        Url of a reference Web page that unambiguously indicates this resource's identity.  # noqa: E501

        :param same_as: The same_as of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._same_as = same_as

    @property
    def is_accessible_for_free(self):
        """Gets the is_accessible_for_free of this ExperimentCreate.  # noqa: E501

        A flag to signal that this asset is accessible at no cost.  # noqa: E501

        :return: The is_accessible_for_free of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._is_accessible_for_free

    @is_accessible_for_free.setter
    def is_accessible_for_free(self, is_accessible_for_free):
        """Sets the is_accessible_for_free of this ExperimentCreate.

        A flag to signal that this asset is accessible at no cost.  # noqa: E501

        :param is_accessible_for_free: The is_accessible_for_free of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._is_accessible_for_free = is_accessible_for_free

    @property
    def version(self):
        """Gets the version of this ExperimentCreate.  # noqa: E501

        The version of this asset.  # noqa: E501

        :return: The version of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ExperimentCreate.

        The version of this asset.  # noqa: E501

        :param version: The version of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._version = version

    @property
    def pid(self):
        """Gets the pid of this ExperimentCreate.  # noqa: E501

        A permanent identifier for the model, for example a digital object identifier (DOI). Ideally a url.  # noqa: E501

        :return: The pid of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this ExperimentCreate.

        A permanent identifier for the model, for example a digital object identifier (DOI). Ideally a url.  # noqa: E501

        :param pid: The pid of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._pid = pid

    @property
    def experimental_workflow(self):
        """Gets the experimental_workflow of this ExperimentCreate.  # noqa: E501

        A human readable description of the overall workflow of the experiment.  # noqa: E501

        :return: The experimental_workflow of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._experimental_workflow

    @experimental_workflow.setter
    def experimental_workflow(self, experimental_workflow):
        """Sets the experimental_workflow of this ExperimentCreate.

        A human readable description of the overall workflow of the experiment.  # noqa: E501

        :param experimental_workflow: The experimental_workflow of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._experimental_workflow = experimental_workflow

    @property
    def execution_settings(self):
        """Gets the execution_settings of this ExperimentCreate.  # noqa: E501

        A human-readable description of the settings under which the experiment was executed.  # noqa: E501

        :return: The execution_settings of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._execution_settings

    @execution_settings.setter
    def execution_settings(self, execution_settings):
        """Sets the execution_settings of this ExperimentCreate.

        A human-readable description of the settings under which the experiment was executed.  # noqa: E501

        :param execution_settings: The execution_settings of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._execution_settings = execution_settings

    @property
    def reproducibility_explanation(self):
        """Gets the reproducibility_explanation of this ExperimentCreate.  # noqa: E501

        A description of how the output of the experiment matches the experiments in the paper.  # noqa: E501

        :return: The reproducibility_explanation of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._reproducibility_explanation

    @reproducibility_explanation.setter
    def reproducibility_explanation(self, reproducibility_explanation):
        """Sets the reproducibility_explanation of this ExperimentCreate.

        A description of how the output of the experiment matches the experiments in the paper.  # noqa: E501

        :param reproducibility_explanation: The reproducibility_explanation of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._reproducibility_explanation = reproducibility_explanation

    @property
    def aiod_entry(self):
        """Gets the aiod_entry of this ExperimentCreate.  # noqa: E501


        :return: The aiod_entry of this ExperimentCreate.  # noqa: E501
        :rtype: AIoDEntryCreate
        """
        return self._aiod_entry

    @aiod_entry.setter
    def aiod_entry(self, aiod_entry):
        """Sets the aiod_entry of this ExperimentCreate.


        :param aiod_entry: The aiod_entry of this ExperimentCreate.  # noqa: E501
        :type: AIoDEntryCreate
        """

        self._aiod_entry = aiod_entry

    @property
    def alternate_name(self):
        """Gets the alternate_name of this ExperimentCreate.  # noqa: E501

        An alias for the item, commonly used for the resource instead of the name.  # noqa: E501

        :return: The alternate_name of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._alternate_name

    @alternate_name.setter
    def alternate_name(self, alternate_name):
        """Sets the alternate_name of this ExperimentCreate.

        An alias for the item, commonly used for the resource instead of the name.  # noqa: E501

        :param alternate_name: The alternate_name of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._alternate_name = alternate_name

    @property
    def application_area(self):
        """Gets the application_area of this ExperimentCreate.  # noqa: E501

        The objective of this AI resource.  # noqa: E501

        :return: The application_area of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._application_area

    @application_area.setter
    def application_area(self, application_area):
        """Sets the application_area of this ExperimentCreate.

        The objective of this AI resource.  # noqa: E501

        :param application_area: The application_area of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._application_area = application_area

    @property
    def badge(self):
        """Gets the badge of this ExperimentCreate.  # noqa: E501

        Labels awarded on the basis of the reproducibility of this experiment.  # noqa: E501

        :return: The badge of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._badge

    @badge.setter
    def badge(self, badge):
        """Sets the badge of this ExperimentCreate.

        Labels awarded on the basis of the reproducibility of this experiment.  # noqa: E501

        :param badge: The badge of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._badge = badge

    @property
    def citation(self):
        """Gets the citation of this ExperimentCreate.  # noqa: E501

        A bibliographic reference.  # noqa: E501

        :return: The citation of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """Sets the citation of this ExperimentCreate.

        A bibliographic reference.  # noqa: E501

        :param citation: The citation of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._citation = citation

    @property
    def contact(self):
        """Gets the contact of this ExperimentCreate.  # noqa: E501

        Contact information of persons/organisations that can be contacted about this resource.  # noqa: E501

        :return: The contact of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this ExperimentCreate.

        Contact information of persons/organisations that can be contacted about this resource.  # noqa: E501

        :param contact: The contact of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._contact = contact

    @property
    def creator(self):
        """Gets the creator of this ExperimentCreate.  # noqa: E501

        Contact information of persons/organisations that created this resource.  # noqa: E501

        :return: The creator of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ExperimentCreate.

        Contact information of persons/organisations that created this resource.  # noqa: E501

        :param creator: The creator of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this ExperimentCreate.  # noqa: E501


        :return: The description of this ExperimentCreate.  # noqa: E501
        :rtype: Text
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExperimentCreate.


        :param description: The description of this ExperimentCreate.  # noqa: E501
        :type: Text
        """

        self._description = description

    @property
    def distribution(self):
        """Gets the distribution of this ExperimentCreate.  # noqa: E501


        :return: The distribution of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this ExperimentCreate.


        :param distribution: The distribution of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._distribution = distribution

    @property
    def has_part(self):
        """Gets the has_part of this ExperimentCreate.  # noqa: E501


        :return: The has_part of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._has_part

    @has_part.setter
    def has_part(self, has_part):
        """Sets the has_part of this ExperimentCreate.


        :param has_part: The has_part of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._has_part = has_part

    @property
    def industrial_sector(self):
        """Gets the industrial_sector of this ExperimentCreate.  # noqa: E501

        A business domain where a resource is or can be used.  # noqa: E501

        :return: The industrial_sector of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._industrial_sector

    @industrial_sector.setter
    def industrial_sector(self, industrial_sector):
        """Sets the industrial_sector of this ExperimentCreate.

        A business domain where a resource is or can be used.  # noqa: E501

        :param industrial_sector: The industrial_sector of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._industrial_sector = industrial_sector

    @property
    def is_part_of(self):
        """Gets the is_part_of of this ExperimentCreate.  # noqa: E501


        :return: The is_part_of of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._is_part_of

    @is_part_of.setter
    def is_part_of(self, is_part_of):
        """Sets the is_part_of of this ExperimentCreate.


        :param is_part_of: The is_part_of of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._is_part_of = is_part_of

    @property
    def keyword(self):
        """Gets the keyword of this ExperimentCreate.  # noqa: E501

        Keywords or tags used to describe this resource, providing additional context.  # noqa: E501

        :return: The keyword of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this ExperimentCreate.

        Keywords or tags used to describe this resource, providing additional context.  # noqa: E501

        :param keyword: The keyword of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._keyword = keyword

    @property
    def license(self):
        """Gets the license of this ExperimentCreate.  # noqa: E501


        :return: The license of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this ExperimentCreate.


        :param license: The license of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._license = license

    @property
    def media(self):
        """Gets the media of this ExperimentCreate.  # noqa: E501

        Images or videos depicting the resource or associated with it.   # noqa: E501

        :return: The media of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this ExperimentCreate.

        Images or videos depicting the resource or associated with it.   # noqa: E501

        :param media: The media of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._media = media

    @property
    def note(self):
        """Gets the note of this ExperimentCreate.  # noqa: E501

        Notes on this AI resource.  # noqa: E501

        :return: The note of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ExperimentCreate.

        Notes on this AI resource.  # noqa: E501

        :param note: The note of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._note = note

    @property
    def relevant_link(self):
        """Gets the relevant_link of this ExperimentCreate.  # noqa: E501

        URLs of relevant resources. These resources should not be part of AIoD (use relevant_resource otherwise). This field should only be used if there is no more specific field.  # noqa: E501

        :return: The relevant_link of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._relevant_link

    @relevant_link.setter
    def relevant_link(self, relevant_link):
        """Sets the relevant_link of this ExperimentCreate.

        URLs of relevant resources. These resources should not be part of AIoD (use relevant_resource otherwise). This field should only be used if there is no more specific field.  # noqa: E501

        :param relevant_link: The relevant_link of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._relevant_link = relevant_link

    @property
    def relevant_resource(self):
        """Gets the relevant_resource of this ExperimentCreate.  # noqa: E501


        :return: The relevant_resource of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._relevant_resource

    @relevant_resource.setter
    def relevant_resource(self, relevant_resource):
        """Sets the relevant_resource of this ExperimentCreate.


        :param relevant_resource: The relevant_resource of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._relevant_resource = relevant_resource

    @property
    def relevant_to(self):
        """Gets the relevant_to of this ExperimentCreate.  # noqa: E501


        :return: The relevant_to of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._relevant_to

    @relevant_to.setter
    def relevant_to(self, relevant_to):
        """Sets the relevant_to of this ExperimentCreate.


        :param relevant_to: The relevant_to of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._relevant_to = relevant_to

    @property
    def research_area(self):
        """Gets the research_area of this ExperimentCreate.  # noqa: E501

        The research area is similar to the scientific_domain, but more high-level.  # noqa: E501

        :return: The research_area of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._research_area

    @research_area.setter
    def research_area(self, research_area):
        """Sets the research_area of this ExperimentCreate.

        The research area is similar to the scientific_domain, but more high-level.  # noqa: E501

        :param research_area: The research_area of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._research_area = research_area

    @property
    def scientific_domain(self):
        """Gets the scientific_domain of this ExperimentCreate.  # noqa: E501

        The scientific domain is related to the methods with which an objective is reached.  # noqa: E501

        :return: The scientific_domain of this ExperimentCreate.  # noqa: E501
        :rtype: object
        """
        return self._scientific_domain

    @scientific_domain.setter
    def scientific_domain(self, scientific_domain):
        """Sets the scientific_domain of this ExperimentCreate.

        The scientific domain is related to the methods with which an objective is reached.  # noqa: E501

        :param scientific_domain: The scientific_domain of this ExperimentCreate.  # noqa: E501
        :type: object
        """

        self._scientific_domain = scientific_domain

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ExperimentCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExperimentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other