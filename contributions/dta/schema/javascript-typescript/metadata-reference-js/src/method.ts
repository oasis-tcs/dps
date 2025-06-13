import { UniqueConcept } from './unique-concept';

export class Method extends UniqueConcept {
  methodCategory: string;
  specificUse: string;

  constructor(code: string, system: string, description: string, methodCategory: string, specificUse: string) {
    super(code, system, description);

    this.methodCategory = methodCategory;
    this.specificUse = specificUse;
  };

  static override default() {
    return new Method("", "", "", "", "");
  };

  static defaultOptions = [
    {
      code: "web-scraping-crawling-textual",
      categoryText: "Web scraping/Crawling",
      specificUseText: "Textual"
    }, {
      code: "web-scraping-crawling-structured",
      categoryText: "Web scraping/Crawling",
      specificUseText: "Structured"
    }, {
      code: "web-scraping-crawling-metadata",
      categoryText: "Web scraping/Crawling",
      specificUseText: "Metadata"
    }, {
      code: "web-scraping-crawling-social-media",
      categoryText: "Web scraping/Crawling",
      specificUseText: "Social media"
    }, {
      code: "web-scraping-crawling-news-articles",
      categoryText: "Web scraping/Crawling",
      specificUseText: "News & articles"
    }, {
      code: "web-scraping-crawling-other",
      categoryText: "Web scraping/Crawling",
      specificUseText: "Other"
    }, {
      code: "feeds-rss-source",
      categoryText: "Feeds",
      specificUseText: "RSS source"
    }, {
      code: "feeds-api-source",
      categoryText: "Feeds",
      specificUseText: "API source"
    }, {
      code: "feeds-real-time-database-info",
      categoryText: "Feeds",
      specificUseText: "Real time database info"
    }, {
      code: "feeds-interval-timed-database-info",
      categoryText: "Feeds",
      specificUseText: "Interval timed database info"
    }, {
      code: "feeds-file-feed-info",
      categoryText: "Feeds",
      specificUseText: "File feed info"
    }, {
      code: "feeds-other",
      categoryText: "Feeds",
      specificUseText: "Other"
    }, {
      code: "syndication-news-feeds",
      categoryText: "Syndication",
      specificUseText: "News feeds"
    }, {
      code: "syndication-financial-feeds",
      categoryText: "Syndication",
      specificUseText: "Financial feeds"
    }, {
      code: "syndication-social-media",
      categoryText: "Syndication",
      specificUseText: "Social media"
    }, {
      code: "syndication-product-service-catalog",
      categoryText: "Syndication",
      specificUseText: "Product/service catalog"
    }, {
      code: "syndication-other",
      categoryText: "Syndication",
      specificUseText: "Other"
    }, {
      code: "data-mining-association-rule",
      categoryText: "Data mining",
      specificUseText: "Association rule"
    }, {
      code: "data-mining-classification",
      categoryText: "Data mining",
      specificUseText: "Classification"
    }, {
      code: "data-mining-clustering",
      categoryText: "Data mining",
      specificUseText: "Clustering"
    }, {
      code: "data-mining-regression",
      categoryText: "Data mining",
      specificUseText: "Regression"
    }, {
      code: "data-mining-anomaly-detection",
      categoryText: "Data mining",
      specificUseText: "Anomaly detection"
    }, {
      code: "data-mining-sequencing",
      categoryText: "Data mining",
      specificUseText: "Sequencing"
    }, {
      code: "data-mining-other",
      categoryText: "Data mining",
      specificUseText: "Other"
    }, {
      code: "machine-generated-mlops-synthetic",
      categoryText: "Machine generated/MLOps",
      specificUseText: "Synthetic"
    }, {
      code: "machine-generated-mlops-generative",
      categoryText: "Machine generated/MLOps",
      specificUseText: "Generative"
    }, {
      code: "machine-generated-mlops-twin",
      categoryText: "Machine generated/MLOps",
      specificUseText: "Twin"
    }, {
      code: "machine-generated-mlops-machine-2-machine",
      categoryText: "Machine generated/MLOps",
      specificUseText: "Machine-2-machine (M2M)"
    }, {
      code: "machine-generated-mlops-ai-inferred",
      categoryText: "Machine generated/MLOps",
      specificUseText: "AI inferred"
    }, {
      code: "machine-generated-mlops-xr",
      categoryText: "Machine generated/MLOps",
      specificUseText: "XR (AR, VR, MR)"
    }, {
      code: "machine-generated-mlops-other",
      categoryText: "Machine generated/MLOps",
      specificUseText: "Other"
    }, {
      code: "sensor-and-iot-output-environmental",
      categoryText: "Sensor and IoT output",
      specificUseText: "Environmental"
    }, {
      code: "sensor-and-iot-output-motion-location",
      categoryText: "Sensor and IoT output",
      specificUseText: "Motion & location"
    }, {
      code: "sensor-and-iot-output-health",
      categoryText: "Sensor and IoT output",
      specificUseText: "Health"
    }, {
      code: "sensor-and-iot-output-biometric",
      categoryText: "Sensor and IoT output",
      specificUseText: "Biometric"
    }, {
      code: "sensor-and-iot-output-energy-consumption",
      categoryText: "Sensor and IoT output",
      specificUseText: "Energy consumption"
    }, {
      code: "sensor-and-iot-output-industrial-sensor",
      categoryText: "Sensor and IoT output",
      specificUseText: "Industrial sensor"
    }, {
      code: "sensor-and-iot-output-vehicle-transportation",
      categoryText: "Sensor and IoT output",
      specificUseText: "Vehicle & transportation"
    }, {
      code: "sensor-and-iot-output-security-surveillance",
      categoryText: "Sensor and IoT output",
      specificUseText: "Security & surveillance"
    }, {
      code: "sensor-and-iot-output-agriculture-environment",
      categoryText: "Sensor and IoT output",
      specificUseText: "Agriculture & environment"
    }, {
      code: "sensor-and-iot-output-other",
      categoryText: "Sensor and IoT output",
      specificUseText: "Other"
    }, {
      code: "social-media-text-based",
      categoryText: "Social media",
      specificUseText: "Text based"
    }, {
      code: "social-media-multimedia",
      categoryText: "Social media",
      specificUseText: "Multimedia"
    }, {
      code: "social-media-reviews-and-ratings",
      categoryText: "Social media",
      specificUseText: "Reviews and ratings"
    }, {
      code: "social-media-updates",
      categoryText: "Social media",
      specificUseText: "Updates"
    }, {
      code: "social-media-q-and-a",
      categoryText: "Social media",
      specificUseText: "Q&As"
    }, {
      code: "social-media-collaborative",
      categoryText: "Social media",
      specificUseText: "Collaborative"
    }, {
      code: "social-media-creative",
      categoryText: "Social media",
      specificUseText: "Creative"
    }, {
      code: "social-media-other",
      categoryText: "Social media",
      specificUseText: "Other"
    }, {
      code: "user-generated-content-clickstream",
      categoryText: "User generated content",
      specificUseText: "Clickstream"
    }, {
      code: "user-generated-content-social-media",
      categoryText: "User generated content",
      specificUseText: "Social media"
    }, {
      code: "user-generated-content-behavior",
      categoryText: "User generated content",
      specificUseText: "Behavior"
    }, {
      code: "user-generated-content-ratings-and-reviews",
      categoryText: "User generated content",
      specificUseText: "Ratings & reviews"
    }, {
      code: "user-generated-content-multimedia",
      categoryText: "User generated content",
      specificUseText: "Multimedia"
    }, {
      code: "user-generated-content-other",
      categoryText: "User generated content",
      specificUseText: "Other"
    }, {
      code: "primary-user-source-survey-questionnaire",
      categoryText: "Primary user source",
      specificUseText: "Survey/Questionnaire"
    }, {
      code: "primary-user-source-interview",
      categoryText: "Primary user source",
      specificUseText: "Interview"
    }, {
      code: "primary-user-source-event",
      categoryText: "Primary user source",
      specificUseText: "Event"
    }, {
      code: "primary-user-source-biometric",
      categoryText: "Primary user source",
      specificUseText: "Biometric"
    }, {
      code: "primary-user-source-focus-group",
      categoryText: "Primary user source",
      specificUseText: "Focus Group"
    }, {
      code: "primary-user-source-other",
      categoryText: "Primary user source",
      specificUseText: "Other"
    }, {
      code: "data-augmentation-na",
      categoryText: "Data augmentation",
      specificUseText: "N/A"
    }, {
      code: "transfer-learning-na",
      categoryText: "Transfer learning",
      specificUseText: "N/A"
    }, {
      code: "simulations-na",
      categoryText: "Simulations",
      specificUseText: "N/A"
    }, {
      code: "other-na",
      categoryText: "Other",
      specificUseText: "N/A"
    }
  ];

  static defaultSystem = "https://dataandtrustalliance.org/DPS/CodeSystem/Method";

  static getDefaultDescription(categoryText: string, specificUseText: string) {
    return (categoryText + " " + specificUseText);
  };

  static getMethodCategories() {
    return new Set(Method.defaultOptions.map((option) => option.categoryText));
  };

  static getSpecificUses(categoryText: string) {
    var specificUses = [""];
    return specificUses.concat(Method.defaultOptions.filter(
      (option) => option.categoryText === categoryText
    ).map(
      (option) => option.specificUseText
    ));
  };
}
